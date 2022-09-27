def get_type_session(session):
    '''
    Kiểm tra dạng của session
    OUTPUT:
        0: admin
        1: user
        2: enterprise
        3: customer
    '''
    if "session_key" in session:

        if session['admin']:
            return 0
        else:
            if "enterprise" in session:
                return 2
            else:
                return 1
    else:
        return 3