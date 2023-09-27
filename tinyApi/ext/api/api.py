
def init_app(app):
    @app.route('/realms', methods=['GET'])
    def getData():
        with open('tinyApi/ext/db/database.json', 'r') as file:
            data = file.read()
        return data