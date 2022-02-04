import requests

def train_call(url):
    res = requests.get(url)
    return (res.status_code)


if __name__ == '__main__':
    train_call(url='https://mailprediction.herokuapp.com/train')