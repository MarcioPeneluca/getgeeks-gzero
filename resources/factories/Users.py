from faker import Faker
fake = Faker()

import bcrypt

def get_hashed_pass(password):
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(8))
    return hashed

def factory_user(target):

    data = {
        "faker": {
            "name": fake.first_name(),
            "lastname": fake.last_name(),
            "email": fake.free_email(),
            "password": "pwd123"
        },
        "wrong_email": {
            "name": "Pedro",
            "lastname": "Lara",
            "email": "pedro_dl*hotmail.com",
            "password": "abc123"
        },
        "login": {
            "name": "Márcio",
            "lastname": "Peneluca",
            "email": "marcio.peneluca@hotmail.com",
            "password": "pwd123"
        },
        "be_geek": {
            "name": "Kim",
            "lastname": "Dotcom",
            "email": "kim@dot.com",
            "password": "pwd123",
            "geek_profile": {
                "whats": "11999999999",
                "desc": "Seu computador está lento? Reiniciando do nada? Talvez seja um vírus, ou algum hardware com defeito. Posso fazer a manutenção no seu PC, formatando, reinstalando o SO, trocando algum componente físico e porque não remover o baidu ou qualquer outro malware",
                "printer_repair": "Sim",
                "work": "Remoto",
                "cost": "100"
            }
        },
        "validations_field_be_geek": {
            "name": "Marabel",
            "lastname": "Encanto",
            "email": "marabel@encanto.com",
            "password": "pwd123",
            "short_desc": {
                "whats": "11999999999",
                "desc": "Formato o seu PC",
                "printer_repair": "Sim",
                "work": "Remoto",
                "cost": "100"
            },
            "long_desc": {
                "whats": "11999999999",
                "desc": "Instalo Distros Ubuntu, Debian, ElementaryOS, PopOS, Linux Mint, Kurumin, Mandrake, Connectiva, Fedora, RedHat, CentOS, Slackware, Gentoo, Archlinux, Kubuntu, Xubuntu, Suze, Mandriva, Edubuntu, KateOS, Sabayon Linux, Manjaro Linux, BigLinux, ZorinOS, Unity",
                "printer_repair": "Sim",
                "work": "Remoto",
                "cost": "100"
            },
            "empty_desc": {
                "whats": "11999999999",
                "desc": "",
                "printer_repair": "Sim",
                "work": "Remoto",
                "cost": "100"
            },
            "empty_whats": {
                "whats": "",
                "desc": "Instalo Distros Ubuntu, Debian, ElementaryOS, PopOS, Linux Mint, Kurumin, Mandrake, Connectiva, Fedora, RedHat, CentOS, Slackware, Gentoo, Archlinux, Kubuntu, Xubuntu, Suze, Mandriva, Edubuntu, KateOS, Sabayon Linux, Manjaro Linux, BigLinux, ZorinOS,Unity",
                "printer_repair": "Não",
                "work": "Ambos",
                "cost": "200"
            },
            "whats_only_ddd": {
                "whats": "71",
                "desc": "Instalo Distros Ubuntu, Debian, ElementaryOS, PopOS, Linux Mint, Kurumin, Mandrake, Connectiva, Fedora, RedHat, CentOS, Slackware, Gentoo, Archlinux, Kubuntu, Xubuntu, Suze, Mandriva, Edubuntu, KateOS, Sabayon Linux, Manjaro Linux, BigLinux, ZorinOS,Unity",
                "printer_repair": "Não",
                "work": "Ambos",
                "cost": "200"
            },
            "whats_ten_digits": {
                "whats": "7199999999",
                "desc": "Instalo Distros Ubuntu, Debian, ElementaryOS, PopOS, Linux Mint, Kurumin, Mandrake, Connectiva, Fedora, RedHat, CentOS, Slackware, Gentoo, Archlinux, Kubuntu, Xubuntu, Suze, Mandriva, Edubuntu, KateOS, Sabayon Linux, Manjaro Linux, BigLinux, ZorinOS,Unity",
                "printer_repair": "Não",
                "work": "Ambos",
                "cost": "200"
            },
            "empty_time_value": {
                "whats": "41999999999",
                "desc": "Instalo Distros Ubuntu, Debian, ElementaryOS, PopOS, Linux Mint, Kurumin, Mandrake, Connectiva, Fedora, RedHat, CentOS, Slackware, Gentoo, Archlinux, Kubuntu, Xubuntu, Suze, Mandriva, Edubuntu, KateOS, Sabayon Linux, Manjaro Linux, BigLinux, ZorinOS,Unity",
                "printer_repair": "Não",
                "work": "Ambos",
                "cost": ""
            },
            "alphanumerics_time_value": {
                "whats": "41999999999",
                "desc": "Instalo Distros Ubuntu, Debian, ElementaryOS, PopOS, Linux Mint, Kurumin, Mandrake, Connectiva, Fedora, RedHat, CentOS, Slackware, Gentoo, Archlinux, Kubuntu, Xubuntu, Suze, Mandriva, Edubuntu, KateOS, Sabayon Linux, Manjaro Linux, BigLinux, ZorinOS,Unity",
                "printer_repair": "Não",
                "work": "Ambos",
                "cost": "lsjd12545"
            },
            "letters_time_value": {
                "whats": "41999999999",
                "desc": "Instalo Distros Ubuntu, Debian, ElementaryOS, PopOS, Linux Mint, Kurumin, Mandrake, Connectiva, Fedora, RedHat, CentOS, Slackware, Gentoo, Archlinux, Kubuntu, Xubuntu, Suze, Mandriva, Edubuntu, KateOS, Sabayon Linux, Manjaro Linux, BigLinux, ZorinOS,Unity",
                "printer_repair": "Não",
                "work": "Ambos",
                "cost": "lsjd"
            },
            "special_characters_time_value": {
                "whats": "41999999999",
                "desc": "Instalo Distros Ubuntu, Debian, ElementaryOS, PopOS, Linux Mint, Kurumin, Mandrake, Connectiva, Fedora, RedHat, CentOS, Slackware, Gentoo, Archlinux, Kubuntu, Xubuntu, Suze, Mandriva, Edubuntu, KateOS, Sabayon Linux, Manjaro Linux, BigLinux, ZorinOS,Unity",
                "printer_repair": "Não",
                "work": "Ambos",
                "cost": "%$#@"
            }
        },
        "short_desc": {
            "name": "Peter",
            "lastname": "Jordam",
            "email": "peter@einerd.com",
            "password": "pwd123",
            "geek_profile": {
                "whats": "21999999999",
                "desc": "Formato o seu PC",
                "printer_repair": "Não",
                "work": "Ambos",
                "cost": "200"
            }
        },
        "long_desc": {
            "name": "Dio",
            "lastname": "Linux",
            "email": "dio@linux.com",
            "password": "pwd123",
            "geek_profile": {
                "whats": "11999999999",
                "desc": "Instalo Distros Ubuntu, Debian, ElementaryOS, PopOS, Linux Mint, Kurumin, Mandrake, Connectiva, Fedora, RedHat, CentOS, Slackware, Gentoo, Archlinux, Kubuntu, Xubuntu, Suze, Mandriva, Edubuntu, KateOS, Sabayon Linux, Manjaro Linux, BigLinux, ZorinOS, Unity",
                "printer_repair": "Não",
                "work": "Remoto",
                "cost": "150"
            }
        },
        "empty_desc": {
            "name": "Jimmy",
            "lastname": "Hendrix",
            "email": "jimmyio@hendrix.com",
            "password": "pwd123",
            "geek_profile": {
                "whats": "11999999999",
                "desc": "",
                "printer_repair": "Não",
                "work": "Remoto",
                "cost": "150"
            }
        },
        "empty_whats": {
            "name": "José",
            "lastname": "Souza",
            "email": "jose@souza.com",
            "password": "pwd123",
            "geek_profile": {
                "whats": "",
                "desc": "Instalo Distros Ubuntu, Debian, ElementaryOS, PopOS, Linux Mint, Kurumin, Mandrake, Connectiva, Fedora, RedHat, CentOS, Slackware, Gentoo, Archlinux, Kubuntu, Xubuntu, Suze, Mandriva, Edubuntu, KateOS, Sabayon Linux, Manjaro Linux, BigLinux, ZorinOS,Unity",
                "printer_repair": "Não",
                "work": "Ambos",
                "cost": "200"
            }
        },
        "whats_only_ddd": {
            "name": "João",
            "lastname": "Pedreira",
            "email": "joao@pedreira.com",
            "password": "pwd123",
            "geek_profile": {
                "whats": "71",
                "desc": "Instalo Distros Ubuntu, Debian, ElementaryOS, PopOS, Linux Mint, Kurumin, Mandrake, Connectiva, Fedora, RedHat, CentOS, Slackware, Gentoo, Archlinux, Kubuntu, Xubuntu, Suze, Mandriva, Edubuntu, KateOS, Sabayon Linux, Manjaro Linux, BigLinux, ZorinOS,Unity",
                "printer_repair": "Não",
                "work": "Ambos",
                "cost": "200"
            }
        },
        "whats_ten_digits": {
            "name": "Marina",
            "lastname": "Lima",
            "email": "marina@lima.com",
            "password": "pwd123",
            "geek_profile": {
                "whats": "7199999999",
                "desc": "Instalo Distros Ubuntu, Debian, ElementaryOS, PopOS, Linux Mint, Kurumin, Mandrake, Connectiva, Fedora, RedHat, CentOS, Slackware, Gentoo, Archlinux, Kubuntu, Xubuntu, Suze, Mandriva, Edubuntu, KateOS, Sabayon Linux, Manjaro Linux, BigLinux, ZorinOS,Unity",
                "printer_repair": "Não",
                "work": "Ambos",
                "cost": "200"
            }
        },
        "empty_time_value": {
            "name": "Vinicio",
            "lastname": "Cruz",
            "email": "vinicio@cruz.com",
            "password": "pwd123",
            "geek_profile": {
                "whats": "41999999999",
                "desc": "Instalo Distros Ubuntu, Debian, ElementaryOS, PopOS, Linux Mint, Kurumin, Mandrake, Connectiva, Fedora, RedHat, CentOS, Slackware, Gentoo, Archlinux, Kubuntu, Xubuntu, Suze, Mandriva, Edubuntu, KateOS, Sabayon Linux, Manjaro Linux, BigLinux, ZorinOS,Unity",
                "printer_repair": "Não",
                "work": "Ambos",
                "cost": ""
            }
        },
        "alphanumerics_time_value": {
            "name": "Moacir",
            "lastname": "Santos",
            "email": "moacir@santos.com",
            "password": "pwd123",
            "geek_profile": {
                "whats": "41999999999",
                "desc": "Instalo Distros Ubuntu, Debian, ElementaryOS, PopOS, Linux Mint, Kurumin, Mandrake, Connectiva, Fedora, RedHat, CentOS, Slackware, Gentoo, Archlinux, Kubuntu, Xubuntu, Suze, Mandriva, Edubuntu, KateOS, Sabayon Linux, Manjaro Linux, BigLinux, ZorinOS,Unity",
                "printer_repair": "Não",
                "work": "Ambos",
                "cost": "lsjd12545"
            }
        },
        "letters_time_value": {
            "name": "Alana",
            "lastname": "Almeida",
            "email": "alana@almeida.com",
            "password": "pwd123",
            "geek_profile": {
                "whats": "41999999999",
                "desc": "Instalo Distros Ubuntu, Debian, ElementaryOS, PopOS, Linux Mint, Kurumin, Mandrake, Connectiva, Fedora, RedHat, CentOS, Slackware, Gentoo, Archlinux, Kubuntu, Xubuntu, Suze, Mandriva, Edubuntu, KateOS, Sabayon Linux, Manjaro Linux, BigLinux, ZorinOS,Unity",
                "printer_repair": "Não",
                "work": "Ambos",
                "cost": "lsjd"
            }
        },
        "special_characters_time_value": {
            "name": "Renato",
            "lastname": "Braga",
            "email": "renato@braga.com",
            "password": "pwd123",
            "geek_profile": {
                "whats": "41999999999",
                "desc": "Instalo Distros Ubuntu, Debian, ElementaryOS, PopOS, Linux Mint, Kurumin, Mandrake, Connectiva, Fedora, RedHat, CentOS, Slackware, Gentoo, Archlinux, Kubuntu, Xubuntu, Suze, Mandriva, Edubuntu, KateOS, Sabayon Linux, Manjaro Linux, BigLinux, ZorinOS,Unity",
                "printer_repair": "Não",
                "work": "Ambos",
                "cost": "%$#@"
            }
        }
    }

    return data[target]