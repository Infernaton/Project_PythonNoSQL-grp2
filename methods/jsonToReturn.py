def json_return(err_code, err_msg):
    return {
        "status": 200,
        "error_code": err_code,
        "error_message": err_msg
    }