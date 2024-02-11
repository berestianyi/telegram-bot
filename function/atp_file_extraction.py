import PyPDF2 as Pdf
from PyPDF2 import PdfReader

dir(Pdf)


def extract_text_from_pdf(path):
    with open(path, "rb") as f:
        reader = PdfReader(f)
        results = []
        for i in range(0, len(reader.pages)):
            page = reader.pages[i]
            text = page.extract_text()
            results.append(text)
        return ' '.join(results)


def is_fop(text_pdf):
    if text_pdf.find("ФОП") != -1:
        return True
    else:
        return False


def fop_name(text_pdf):
    name_start = text_pdf.find("ФОП") + len("ФОП ")
    name_end = text_pdf.find("Витяг з Єдиного державного реєстру") - 1

    return text_pdf[name_start:name_end]


def tov_name(text_pdf):
    name_start = text_pdf.find("ВІДПОВІДАЛЬНІСТЮ") + len("ВІДПОВІДАЛЬНІСТЮ ")
    name_end = text_pdf.find("Код:") - 1

    return text_pdf[name_start:name_end]


def tov_director_name(text_pdf):
    start = text_pdf.find("Керівник:") + len("Керівник: ")
    index_text = text_pdf[start:]
    end = index_text.find("\n")

    return index_text[:end]


def personal_info(text_pdf):
    if text_pdf.find("Контактна інформація") != -1 and text_pdf.find("Дані про взяття на облік") != -1:
        index_start = text_pdf.find("Контактна інформація") + len("Контактна інформація ")
        index_end = text_pdf.find("Дані про взяття на облік")
        return text_pdf[index_start:index_end]
    elif text_pdf.find("Контактна інформація") != -1 and text_pdf.find("Дані про взяття на облік") == -1:
        index_start = text_pdf.find("Контактна інформація") + len("Контактна інформація ")
        return text_pdf[index_start:]
    else:
        return None


def phone_fop_search(text_pdf):
    if text_pdf.find("Телефони:") != -1 and text_pdf.find("Email:") != -1:
        phone_start = text_pdf.find("Телефони:") + len("Телефони:")
        phone_end = text_pdf.find("Email:") - 1
        return text_pdf[phone_start:phone_end]
    if text_pdf.find("Телефони:") != -1 and text_pdf.find("Email:") == -1:
        phone_start = text_pdf.find("Телефони:") + len("Телефони:")
        return text_pdf[phone_start:]
    else:
        return None


def phone_tov_search(text_pdf):
    if text_pdf.find("Телефон:") != -1 and text_pdf.find("Email:") != -1:
        phone_start = text_pdf.find("Телефон:") + len("Телефон:")
        phone_end = text_pdf.find("Email:") - 1
        return text_pdf[phone_start:phone_end]
    if text_pdf.find("Телефон:") != -1 and text_pdf.find("Email:") == -1:
        phone_start = text_pdf.find("Телефон:") + len("Телефон:")
        return text_pdf[phone_start:]
    else:
        return None


def email_search(text_pdf):
    if text_pdf.find("Email:") != -1:
        email_start = text_pdf.find("Email:") + len("Email:")
        return text_pdf[email_start:]
    else:
        return None


def address_search(text_pdf):
    if text_pdf.find("Адреса:") != -1:
        index_start = text_pdf.find("Адреса:") + len("Адреса: ")
        index_end = text_pdf.find("Статус:") - 1

        return text_pdf[index_start:index_end]
    else:
        return None


def id_code_fop_search(text_pdf):
    index_start = text_pdf.find("Ідентифікаційний код:") + len("Ідентифікаційний код: ")
    index_end = index_start + 10

    return text_pdf[index_start:index_end]


def id_code_tov_search(text_pdf):
    index_start = text_pdf.find("Код:") + len("Код: ")
    index_end = index_start + 8

    return text_pdf[index_start:index_end]


def pdf_extraction(file_path) -> dict:

    text = extract_text_from_pdf(file_path)
    half_of_text = text[0:500]

    if is_fop(half_of_text):
        name = fop_name(half_of_text).rstrip().replace("\n", " ")
        code = id_code_fop_search(half_of_text).rstrip().replace("\n", " ")
        address = address_search(text).rstrip().replace("\n", " ")
        company = None
        if personal_info(text) is None:
            email = phone = None
        else:
            phone = phone_fop_search(personal_info(text))
            email = email_search(personal_info(text))
            if phone is not None:
                phone = phone.rstrip().replace("\n", " ")
            if email is not None:
                email = email.rstrip().replace("\n", " ")
    else:
        company = tov_name(half_of_text).rstrip().replace("\n", " ")
        code = id_code_tov_search(text).rstrip().replace("\n", " ")
        address = address_search(text).rstrip().replace("\n", " ")
        name = tov_director_name(text)
        if personal_info(text) is None:
            email = phone = None
        else:
            phone = phone_tov_search(personal_info(text))
            email = email_search(personal_info(text))
            if phone is not None:
                phone = phone.rstrip().replace("\n", " ")
            if email is not None:
                email = email.rstrip().replace("\n", " ")

    pdf_data = {"name": name, "company": company,
                "code": code, "address": address,
                "email": email, "phone": phone}

    return pdf_data


def is_tov(file_path):
    text = extract_text_from_pdf(file_path)
    half_of_text = text[0:500]
    if is_fop(half_of_text):
        return False
    else:
        return True


def extraction_of_tov_name(file_path):
    text = extract_text_from_pdf(file_path)
    return tov_director_name(text)
