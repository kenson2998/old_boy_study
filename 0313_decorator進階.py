
def auth(auth_type):
    print("auth func:",auth_type)

    def out_wrapper(func):
        def wrapper(*args, **kwargs):
            if auth_type == "local":
                username = input("Username:")
                password = input("Password:")
                if username == "leon" and password == "abc123":
                    print("weclome ,login success!")
                    res = func(*args, **kwargs)
                    return res #會影響return 是否有值
                else:

                    exit("Invalid username or password")
            elif auth_type == "ladp":
                print("沒有ladp")
        return wrapper
    return out_wrapper

def index():
    print("this is index page")

@auth(auth_type = "local")
def form_page():
    print("this is form page")
    return "form _page"

@auth(auth_type = "ladp")
def bbs():
    print("this is bbs page")

index()
form_page()
print(form_page())
bbs()