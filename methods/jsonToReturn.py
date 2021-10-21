def json_return(err_code, err_msg, status = 200):
    """
    A json template to return when a error occurred

    :param err_code: the code of the error
    :param err_msg: the message of the error
    :param status: the status of the request
    :return: a json template of the response
    """
    return {
        "status": status,
        "error_code": err_code,
        "error_message": err_msg
    }