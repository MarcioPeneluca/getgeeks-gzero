*Settings*
Documentation       Authentication actions

*Variables*
${INPUT_EMAIL}     id=email
${INPUT_PASS}      id=password

*Keywords*
Go To Login Page
    Go To       ${BASE_URL}

    Wait For Elements State      css=.login-form    visible     5

Fill Credentials
    [Arguments]     ${user}

    Fill Text       ${INPUT_EMAIL}        ${user}[email]
    Fill Text       ${INPUT_PASS}         ${user}[password]

Submit Credentials
    Click           css=.submit-button >> text=Entrar

User Should Be Logged In
    [Arguments]     ${user}

    ${element}      Set Variable        css=a[href="/profile"]
    ${expect_fullname}     Set Variable      ${user}[name] ${user}[lastname]

    Wait For Elements State     ${element}      visible     5
    Get Text                    ${element}      equal       ${expect_fullname}


Should Be Type Email
    Get Property       ${INPUT_EMAIL}        type        equal       email


Empty Field
    [Arguments]     ${expect_message}

    ${campo_mensagem}       Set Variable    css=.error >> text=${expect_message}

    Wait For Elements State     css=.login-form     visible     5
    Get Text        ${campo_mensagem}       equal       ${expect_message}

Empty Required Fields
    [Arguments]     ${user}

    ${msg_email}       Set Variable    css=.error >> text=${user}[msg1]
    ${msg_pass}        Set Variable    css=.error >> text=${user}[msg2]
    
    Wait For Elements State     css=.login-form     visible     5
    Get Text        ${msg_email}       equal       ${user}[msg1]
    Get Text        ${msg_pass}        equal       ${user}[msg2]