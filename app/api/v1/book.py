from app.libs.subprint import Subprint

api = Subprint('book')

@api.route('/get')
def get_book():
    return 'get book'

@api.route('/create')
def create_book():
    return 'create book111'