http_status = 500

match http_status:
    case 200 | 201:
        print("success")
    case 400:
        print("Bad Request")
    case 500 | 501:
        print("Server Error")
    case _:
        print("unknown")