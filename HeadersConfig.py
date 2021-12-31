class config:
    def get_header(self):
        request_header = {'device': 'vivo+Y55',
                        'od': '',
                        'deviceId': '1e355c3cf97e709ee24a6fb8f9066f7e',
                        'mi': '865226030586858',
                        'fr': 'ANDROID',
                        'ch': 'ALIBABA',
                        'umid': '',
                        'noReco': '0',
                        'egid': 'DFP66AD41BCEF72E3147882C5004A3305BEEC0F63D9CE14DF52FE0F3CBB50358',
                        'md': 'vivo Y55',
                        'appver': '2.5.8.20580',
                        've': '2.5.8.20580',
                        'channel': 'ALIBABA',
                        'type': 'fairyTale',
                        'sr': '720*1280',
                        'wifi': '"APUS-Vip"',
                        'isdg': '0',
                        'ver_code': '20580',
                        'did': 'ANDROID_ba45c96011b25866',
                        'boardPlatform': 'msm8937',
                        'app': 'm2u',
                        'os': 'ANDROID_6.0.1',
                        'platform': 'android',
                        'brand': 'vivo',
                        'globalid': 'DFP66AD41BCEF72E3147882C5004A3305BEEC0F63D9CE14DF52FE0F3CBB50358'
                        }
        return request_header


if __name__ == "__main__":
    cc = config()
    print(cc.get_header())
