#!/usr/bin/env python3
"""Build the RED Skill folder ZIP and a self-contained Markdown fallback."""
from pathlib import Path, PurePosixPath
import hashlib
import posixpath
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'publishing/red-skill'
NAME = 'pte-coach-zh'
LINK = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
UPSTREAM = 'https://github.com/alvinwo/pte-skills/blob/main/'


def external(url):
    return '://' in url or url.startswith(('mailto:', '#'))


def build():
    # Reuse maintained Chinese sources, retaining their relative directory shape.
    source_paths = sorted(p for folder in ('shared', 'skills', 'examples')
                          for p in (ROOT / 'zh-CN' / folder).glob('*.md'))
    targets = {p.relative_to(ROOT).as_posix():
               'references/' + p.relative_to(ROOT / 'zh-CN').as_posix()
               for p in source_paths}
    data_path = 'data/au-home-affairs-english-requirements.json'
    targets[data_path] = 'references/data/au-home-affairs-english-requirements.json'
    files = {}
    for p in source_paths:
        source = p.relative_to(ROOT).as_posix()
        target = targets[source]

        def rewrite(match):
            label, url = match.groups()
            if external(url):
                return match.group(0)
            path, marker, anchor = url.partition('#')
            resolved = posixpath.normpath(posixpath.join(posixpath.dirname(source), path))
            assert (ROOT / resolved).is_file(), (source, url)
            if resolved in targets:
                href = posixpath.relpath(targets[resolved], posixpath.dirname(target))
            else:
                href = UPSTREAM + resolved
            return f'[{label}]({href}' + (f'#{anchor}' if marker else '') + ')'

        files[target] = LINK.sub(rewrite, p.read_text()).encode()
    files[targets[data_path]] = (ROOT / data_path).read_bytes()
    files['SKILL.md'] = (DEST / NAME / 'SKILL.md').read_bytes()
    files['LICENSE.txt'] = (ROOT / 'LICENSE').read_bytes()

    for name, content in files.items():
        output = DEST / NAME / name
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(content)

    # Validate links against the archive, not the source checkout.
    for name, content in files.items():
        if not name.endswith('.md'):
            continue
        for _, url in LINK.findall(content.decode()):
            if external(url):
                continue
            resolved = posixpath.normpath(posixpath.join(posixpath.dirname(name), url.split('#')[0]))
            assert resolved in files, (name, url)

    archive = DEST / f'{NAME}.zip'
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for name, content in sorted(files.items()):
            entry = zipfile.ZipInfo(f'{NAME}/{name}', (2026, 9, 11, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            z.writestr(entry, content)
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        assert all(not PurePosixPath(n).is_absolute() and '..' not in PurePosixPath(n).parts
                   for n in z.namelist())

    # Inline all runtime references so a single-file upload has no missing dependencies.
    ordered = ['SKILL.md'] + sorted(n for n in files if n != 'SKILL.md')
    anchors = {n: f'ref-{i:02d}' for i, n in enumerate(ordered)}
    sections = []
    for name in ordered:
        content = files[name].decode()
        if name == 'SKILL.md':
            content = content.replace('如果参考文件缺失，说明缺的是哪一页，请学生补充文件；不要假装链接内容已经读过。',
                '本文件是自包含版本。下方各节已内嵌全部参考内容；按请求定位对应章节，不需要联网读取本地参考页。不要把整份教练参考资料先展示给学生。')

        def inline_link(match):
            label, url = match.groups()
            if external(url):
                return match.group(0)
            resolved = posixpath.normpath(posixpath.join(posixpath.dirname(name), url.split('#')[0]))
            return f'[{label}](#{anchors[resolved]})'

        content = LINK.sub(inline_link, content)
        if name == 'SKILL.md':
            sections.append(content)
        else:
            if name.endswith('.json'):
                content = '```json\n' + content.rstrip() + '\n```\n'
            sections.append(f'\n<a id="{anchors[name]}"></a>\n\n## 内嵌参考：{name}\n\n' + content)
    single = DEST / 'single-file' / NAME / 'SKILL.md'
    single.parent.mkdir(parents=True, exist_ok=True)
    single.write_text('\n'.join(sections))
    # In the fallback, every local link must be an existing inline anchor.
    text = single.read_text()
    anchor_ids = set(re.findall(r'<a id="([^"]+)"', text))
    for _, url in LINK.findall(text):
        if url.startswith('#'):
            assert url[1:] in anchor_ids, url
        else:
            assert '://' in url or url.startswith('mailto:'), url
    assert len(list((ROOT / 'zh-CN/skills').glob('*.md'))) == 21
    assert max(map(len, files.values())) < 10_000_000
    assert sum(map(len, files.values())) < 30_000_000
    assert single.stat().st_size < 10_000_000
    for output in (archive, single):
        print(f'{output.relative_to(ROOT)}: {output.stat().st_size} bytes; '
              f'SHA256 {hashlib.sha256(output.read_bytes()).hexdigest()}')
    print(f'Validated {len(files)} package files, 21 task guides, archive links and inline anchors.')


if __name__ == '__main__':
    build()
