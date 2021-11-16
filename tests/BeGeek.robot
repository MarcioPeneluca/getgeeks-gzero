*Settings*
Documentation       Be Geek teste suíte

Resource            ${EXECDIR}/resources/Base.robot

Test Setup          Start Session
Test Teardown       Finish Session



*Test Cases*
Be a Geek
    
    ${user}     Factory User    be_geek
    Do Login    ${user}

    Go To Geek Form 
    Fill Geek Form      ${user}[geek_profile]
    Submit Geek Form
    Geek Form Should Be Success


Short Description
    
    ${user}     Factory User    validations_field_be_geek
    
    Do Login    ${user}
    
    Go To Geek Form 
    Fill Geek Form      ${user}[short_desc]
    Submit Geek Form
    Alert Span Should Be   A descrição deve ter no minimo 80 caracteres

Long Description
    [Tags]      long_desc

    ${user}     Factory User    validations_field_be_geek
    
    Do Login    ${user}

    Go To Geek Form 
    Fill Geek Form      ${user}[long_desc]
    Submit Geek Form
    Alert Span Should Be   A descrição deve ter no máximo 255 caracteres

Empty Description
    [Tags]      empty_desc

    ${user}     Factory User    validations_field_be_geek
    
    Do Login    ${user}

    Go To Geek Form 
    Fill Geek Form      ${user}[empty_desc]
    Submit Geek Form
    Alert Span Should Be   Informe a descrição do seu trabalho


Empty Whats

    ${user}     Factory User    validations_field_be_geek
    
    Do Login    ${user}

    Go To Geek Form 
    Fill Geek Form      ${user}[empty_whats]
    Submit Geek Form
    Alert Span Should Be   O Whatsapp deve ter 11 digitos contando com o DDD

Whats Only DDD

    ${user}     Factory User    validations_field_be_geek
    
    Do Login    ${user}

    Go To Geek Form 
    Fill Geek Form      ${user}[whats_only_ddd]
    Submit Geek Form
    Alert Span Should Be   O Whatsapp deve ter 11 digitos contando com o DDD

Whats With Ten Digits

    ${user}     Factory User    validations_field_be_geek
    
    Do Login    ${user}

    Go To Geek Form 
    Fill Geek Form      ${user}[whats_ten_digits]
    Submit Geek Form
    Alert Span Should Be   O Whatsapp deve ter 11 digitos contando com o DDD

Empty Time Value

    ${user}     Factory User    validations_field_be_geek
    
    Do Login    ${user}

    Go To Geek Form 
    Fill Geek Form      ${user}[empty_time_value]
    Submit Geek Form
    Alert Span Should Be   Valor hora deve ser numérico

Hour Value With Alphanumerics

    ${user}     Factory User    validations_field_be_geek
    
    Do Login    ${user}

    Go To Geek Form 
    Fill Geek Form      ${user}[alphanumerics_time_value]
    Submit Geek Form
    Alert Span Should Be   Valor hora deve ser numérico

Hour Value With Letters

    ${user}     Factory User    validations_field_be_geek
    
    Do Login    ${user}

    Go To Geek Form 
    Fill Geek Form      ${user}[letters_time_value]
    Submit Geek Form
    Alert Span Should Be   Valor hora deve ser numérico

Hour Value With Special Characters

    ${user}     Factory User    validations_field_be_geek
    
    Do Login    ${user}

    Go To Geek Form 
    Fill Geek Form      ${user}[special_characters_time_value]
    Submit Geek Form
    Alert Span Should Be   Valor hora deve ser numérico





# Validations Field Be Geek

#     @{expected_mensagens}         Create List     
#     ...                           A descrição deve ter no minimo 80 caracteres    
#     ...                           A descrição deve ter no máximo 255 caracteres
#     ...                           Informe a descrição do seu trabalho
#     ...                           O Whatsapp deve ter 11 digitos contando com o DDD
#     ...                           Valor hora deve ser numérico

#     ${user}     Factory User    special_characters_time_value

#     Submit Geek Form
#     Alert Span Should Be          ${expected_mensagens}





# Desafio final do módulo PRO

# 1- Whatsapp em branco
# 2- Whatsapp somente DDD
# 3- Whatsapp com 10 digitos
# 4- Descrição em branco
# 5- Valor hora em branco
# 6- Valor hora com alphanuméricos
# 7- Valor hora com letras
# 8- Valor hora com caracteres especiais

# Dica 1: Use o modelo de template de teste
# Dica 2: O login ficará melhor se for executado uma única vez para todos os comportamentos.

