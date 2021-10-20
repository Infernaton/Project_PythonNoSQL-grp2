def json_return(err_code, err_msg):
    """
    A json template to return when a error occurred

    :param err_code: the code of the error
    :param err_msg: the message of the error
    :return: a json template of the response
    """
    return {
        "status": 200,
        "error_code": err_code,
        "error_message": err_msg
    }