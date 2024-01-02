from flask import Flask, render_template

app = Flask(__name__)

channels = {
    # Tnt Sports
    'bbtsp1': 'TNT SPORTS 1',
    'bbtsp2': 'TNT SPORTS 2',
    'bbtsp3': 'TNT SPORTS 3',
    'bbtespn': 'TNT SPORTS 4',

    # Sky Sports
    'skysme': 'SKY SPORTS MAIN EVENT',
    'skyscric': 'SKY SPORTS CRICKET',
    'skysfott': 'SKY SPORTS FOOTBALL',
    'skysare': 'SKY SPORTS ARENA',
    'skysact': 'SKY SPORTS ACTION',
    'skysgol': 'SKY SPORTS GOLF',
    'skysprem': 'SKY SPORTS PREMIER LEAGUE',
    'skysfor1': 'SKY SPORTS F1',
    'skysmixx': 'SKY SPORTS MIX',
    'skysnewsuk': 'SKY SPORTS NEWS',

    # PTV
    'ptvpk': 'PTV SPORTS LIVE',

    # SUPERSPORT
    'superspcric': 'SUPERSPORT CRICKET',
    'superpremierleague': 'SUPERSPORT PREMIER LEAGUE',
    'superlaliga': 'SUPERSPORT LALIGA',
    'superspfb': 'SUPERSPORT FOOTBALL',
    'superspaction': 'SUPERSPORT ACTION',
    'supergs': 'SUPERSPORT GRANDSTAND',

    # TSN
    'tsn1ca': 'TSN 1',
    'tsn2ca': 'TSN 2',
    'tsn3ca': 'TSN 3',
    'tsn4ca': 'TSN 4',
    'tsn5ca': 'TSN 5',

    # VIAPLAY
    'viaplaysp2': 'VIAPLAY SPORTS 2',
    'viaplayextra': 'VIAPLAY EXTRA',
}


@app.route('/')
def home():
    return render_template(
        "home.html",
        channels=channels,
    )


@app.route('/<string:stream_channel>')
def stream(stream_channel):
    if stream_channel and stream_channel != '':
        return render_template("player.html",
                               strem_channel=stream_channel,
                               )
    return 'No Stream'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port='4000')
