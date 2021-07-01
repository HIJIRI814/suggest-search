import requests
import sys
import time

additional_words = [
    'あ', 'い', 'う', 'え', 'お',
    'か', 'き', 'く', 'け', 'こ',
    'さ', 'し', 'す', 'せ', 'そ',
    'た', 'ち', 'つ', 'て', 'と',
    'な', 'に', 'ぬ', 'ね', 'の',
    'は', 'ひ', 'ふ', 'へ', 'ほ',
    'ま', 'み', 'む', 'め', 'も',
    'や', 'ゆ', 'よ',
    'ら', 'り', 'る', 'れ', 'ろ',
    'わ', 'を', 'ん',
]


def export_csv(keyword, data):
    search_word = data[0]
    words = data[1]
    with open(f'result_{keyword}.txt', mode='a') as f:
        f.write(f'----- {search_word} -----\n')
        [f.write(word + '\n') for word in words]


def search_sugget_words(keyword, kana=''):
    path = f'http://clients1.google.com/complete/search?hl=en&ds=yt&client=firefox&q={keyword} {kana}'
    result = requests.get(path)
    return result.json()


def main():
    # sns = sys.argv[0]
    keyword = sys.argv[1]
    result = search_sugget_words(keyword)
    export_csv(keyword, result)
    time.sleep(1)
    for word in additional_words:
        result = search_sugget_words(keyword, word)
        export_csv(keyword, result)
        time.sleep(1)


if __name__ == '__main__':
    main()
