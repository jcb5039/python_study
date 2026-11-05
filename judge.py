"""입출력 문제 채점기

사용법 (python-study 폴더에서):
    python3 judge.py exercises/ch05/ex02_sum.py

문제 파일을 실행하면서 cases/ 폴더에 준비된 입력을 넣어 주고,
출력이 정답과 같은지 비교해서 ✅/❌로 알려 줘요.

이 파일은 고치지 않아도 돼요.
"""

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def normalize(text):
    # 줄 끝 공백과 맨 끝 빈 줄은 무시하고 비교해요.
    lines = [line.rstrip() for line in text.strip('\n').split('\n')]
    return '\n'.join(lines).rstrip('\n')


def indent(text, limit=15):
    text = text.rstrip('\n')
    if text == '':
        return '    (없음)'
    lines = text.split('\n')
    shown = '\n'.join('    ' + line for line in lines[:limit])
    if len(lines) > limit:
        shown += f'\n    ... (아래 {len(lines) - limit}줄 생략)'
    return shown


def first_difference(mine, expected):
    # 몇 번째 줄부터 다른지 알려 줘요.
    a = normalize(mine).split('\n')
    b = normalize(expected).split('\n')
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            return f'  → {i + 1}번째 줄이 달라요. 정답: {b[i]!r} / 내 출력: {a[i]!r}'
    return f'  → 줄 수가 달라요. 정답: {len(b)}줄 / 내 출력: {len(a)}줄'


def main():
    if len(sys.argv) != 2:
        print('사용법: python3 judge.py 문제파일.py')
        print('예시:   python3 judge.py exercises/ch05/ex02_sum.py')
        return

    target = Path(sys.argv[1]).resolve()
    if not target.exists():
        print(f'파일을 찾을 수 없어요: {sys.argv[1]}')
        print('python-study 폴더에서 실행했는지, 파일 이름이 맞는지 확인해 보세요.')
        return

    chapter = target.parent.name  # 예: ch05
    problem = target.stem.split('_')[0]  # 예: ex02
    case_dir = ROOT / 'cases' / chapter / problem
    out_files = sorted(case_dir.glob('*.out'))
    if not out_files:
        print(f'이 문제는 judge.py로 채점하는 문제가 아니에요: {chapter}/{target.name}')
        print(f'대신 이렇게 실행해 보세요: python3 {sys.argv[1]}')
        return

    env = dict(os.environ, PYTHONIOENCODING='utf-8')
    passed = 0
    for number, out_path in enumerate(out_files, start=1):
        in_path = out_path.with_suffix('.in')
        given = in_path.read_text(encoding='utf-8') if in_path.exists() else ''
        expected = out_path.read_text(encoding='utf-8')

        try:
            result = subprocess.run(
                [sys.executable, str(target)],
                input=given,
                capture_output=True,
                text=True,
                encoding='utf-8',
                timeout=5,
                env=env,
            )
        except subprocess.TimeoutExpired:
            print(f'❌ {number}번: 5초 안에 끝나지 않았어요.')
            print('   반복문이 끝나지 않거나, input()을 입력보다 많이 부르고 있지 않은지 확인해 보세요.')
            continue

        if result.returncode != 0:
            print(f'❌ {number}번: 실행하다가 에러가 났어요.')
            print('  [넣어 준 입력]')
            print(indent(given))
            print('  [에러 메시지] (맨 아래 줄부터 읽어 보세요)')
            print(indent(result.stderr))
            if 'EOFError' in result.stderr:
                print('  힌트: input()을 입력 줄 수보다 많이 불렀어요.')
            continue

        if normalize(result.stdout) == normalize(expected):
            print(f'✅ {number}번')
            passed += 1
        else:
            print(f'❌ {number}번: 출력이 달라요.')
            print('  [넣어 준 입력]')
            print(indent(given))
            print('  [정답 출력]')
            print(indent(expected))
            print('  [내 출력]')
            print(indent(result.stdout))
            print(first_difference(result.stdout, expected))

    print('-' * 30)
    if passed == len(out_files):
        print(f'🎉 {passed}/{len(out_files)} 전부 통과!')
    else:
        print(f'{passed}/{len(out_files)} 통과')


main()
