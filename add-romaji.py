import cutlet
import csv
import sys

katsu = cutlet.Cutlet()
katsu.add_exception("・", "") # this is used like a space
katsu.add_exception("アートディンク", "Artdink")
katsu.add_exception("ヒーローズ", "Heroes")
katsu.add_exception("マイト", "Might")
katsu.add_exception("キャロット", "Carrot")
katsu.add_exception("ムーンライト", "Moonlight")
katsu.add_exception("麻雀", "Mahjong")
katsu.add_exception("アスキー", "ASCII")
katsu.add_exception("フォース", "Force")

fields = ['発売元', 'タイトル名', 'システム', 'メディア', 'カタログナンバー', 'メーカー番号', 'バーコード', '難／欠', 'ローマ字']

POST = [
        ("Iii", "Ii"),
        ("Ii", "II"),
        ("Ascii", "ASCII"),
        ("Msx", "MSX"),
        ("Dos", "DOS"),
        ]

with open(sys.argv[1]) as infile:
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(sys.stdout, fields)

    print(",".join(fields))
    for row in reader:
        if not row.get('ローマ字'):
            title = row['タイトル名']
            # Mark with emoji to show it's automatic
            romaji = katsu.romaji(title, title=True)

            # a little post processing
            for before, after in POST:
                romaji = romaji.replace(before, after)

            row['ローマ字'] = '🤖' + romaji

        writer.writerow(row)






