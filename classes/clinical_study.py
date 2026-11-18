import utils.utils as u


class ClinicalStudy:
    def __init__(self, authors, title, url, publication, subject, priority, language, year):
        self.author_string = authors
        self.title = title.strip()
        self.url = url.strip()
        self.publication = publication.strip()
        self.subject = subject.strip()
        self.priority = u.convert_to_int(priority)
        self.language = language
        self.year = year

        self.split_authors()
        self.get_language_string()

    def split_authors(self):
        if self.author_string is None:
            self.authors = []
        else:
            self.authors = self.author_string.split(",")
            for i in range(len(self.authors)):
                self.authors[i] = self.authors[i].strip()

    def get_language_string(self):
        if self.language == "English":
            self.language_string = ""
        else:
            self.language_string = f" (in {self.language})"

    def as_dict(self):
        ret = {
            "subject": self.subject,
            "authors": self.authors,
            "title": self.title,
            "url": self.url,
            "publication": self.publication,
            "priority": self.priority,
            "language": self.language,
            "year": self.year,
        }
        return ret

    def as_row(self):
        QUOTE = '"'
        COMMA = ","
        NL = "\n"
        ret = ""
        ret += QUOTE + self.subject + QUOTE + COMMA
        ret += QUOTE + ", ".join(self.authors).replace('"', "'") + QUOTE + COMMA
        ret += QUOTE + self.title + QUOTE + COMMA
        ret += QUOTE + self.url + QUOTE + COMMA
        ret += QUOTE + self.publication + QUOTE + COMMA
        ret += QUOTE + str(self.priority) + QUOTE + COMMA
        ret += QUOTE + self.language + QUOTE + NL

        return ret

    def as_html(self):
        authors = ", ".join(self.authors).replace('"', "'")
        ret = "\t<li>"
        ret += f"<span class='authors'>{authors}</span> "
        ret += "<span class='title'><a href='{url}' target='_blank'>{title}{language}{accessibility}</a></span> ".format(
            url=self.url,
            title=self.title,
            language=self.language_string,
            accessibility='<i class="fas fa-external-link-alt" aria-hidden="true"></i><span class="screen-reader-text"> opens a new window</span>',
        )
        ret += "<span class='publication'>" + self.publication + "</span>"
        ret += "</li>\n"

        return ret
