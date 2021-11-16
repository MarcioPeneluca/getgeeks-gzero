*Settings*
Documentation       Login test suite

Resource    ${EXECDIR}/resources/Base.robot

Test Setup      Start Session
Test Teardown   Finish Session

*Test Cases*
User Login

    ${user}                     Factory User    login
    
    Go To Login Page
    Fill Credentials            ${user}
    Submit Credentials
    User Should Be Logged In        ${user}

Incorrect Pass
    [Tags]          inv_pass
    ${user}         Create Dictionary       email=marcio.peneluca@hotmail.com       password=abc123

    Go To Login Page
    Fill Credentials        ${user}
    Submit Credentials
    Modal Content Should Be     Usuário e/ou senha inválidos.

User Not Found
    [Tags]          user_404
    ${user}         Create Dictionary       email=marcio.peneluca@404.com       password=abc123

    Go To Login Page
    Fill Credentials        ${user}
    Submit Credentials
    Modal Content Should Be     Usuário e/ou senha inválidos.

Incorrect Email
    [Tags]          inv_email
    ${user}         Create Dictionary       email=marcio.peneluca.com.br       password=abc123

    Go To Login Page
    Fill Credentials        ${user}
    Submit Credentials
    Should Be Type Email 

Required Email
    [Tags]          req_email
    ${user}         Create Dictionary       email=${EMPTY}      password=abc123

    Go To Login Page
    Fill Credentials        ${user}
    Submit Credentials
    Alert Span Should Be      E-mail obrigatório

Required Pass
    [Tags]          req_pass
    ${user}         Create Dictionary       email=marcio.peneluca@hotmail.com       password=${EMPTY}

    Go To Login Page
    Fill Credentials        ${user}
    Submit Credentials
    Alert Span Should Be       Senha obrigatória

Required Fields
    [Tags]          req_fields

    @{expected_alerts}      Create List
    ...                     E-mail obrigatório
    ...                     Senha obrigatória

    Go To Login Page
    Submit Credentials
    Alert Spans Should Be       ${expected_alerts}