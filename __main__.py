import yaml

class Storage:
    def __init__():
        self.apps = []

    def load_from_yaml(ymlfile):
        with open(ymlfile, "r") as file:
            data = yaml.safe_load(file)

    def yaml_data_to_list(data):
        for item

    def get_app_by_id(id):
        for app in self.apps:
            if app.id = id:
                return app
        return False

    def get_apps_by_category(category):
        apps = []
        for app in self.apps:
            if app.category = category:
                apps.append(app)
        return apps

    def get_apps_by_search(search_term):
        terms = search_term.split()
        apps = []
        matched_name = []
        matched_description = []
        matched_url = []

        for term in terms:
            for app in self.apps:
                if term in app.name:
                    if !app_id_exists(app.id):
                        matched_name.append(app)
                if term in app.comment:
                    if !app_id_exists(app.id):
                        matched_comment.append(app)
                if term in app.description:
                    if !app_id_exists(app.id):
                        matched_description.append(app)

        apps = matched_name
        for app in matched_description:
            if !app_id_exists(app.id):
                apps.append(app)
        for app in matched_url:
            if !app_id_exists(app.id):
                apps.append(app)

        return apps

    def add_app(app):
        if !app_id_exists(app.id):
            self.apps.append(app)

    def app_id_exists(id):
        for app in self.apps:
            if app.id = id:
                return True
        return False

class WebApp:
    def __init__(id, name, url, comment, description, catagory, price):
        self.id = ""
        self.name = ""
        self.url = ""
        self.comment = ""
        self.description = ""
        self.category = ""
        self.price = ""
