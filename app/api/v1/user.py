from app.libs.subprint import Subprint

api = Subprint('user')

@api.route('/get')
def get_user():
    return 'get user'

