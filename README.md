# Ö1Py

Ö1Py is a radio program scraper for the Austrian radio station [Ö1](https://en.wikipedia.org/wiki/%C3%961) written in Python.
It can be used to obtain a tabular representation of the radio program as well as URLs for the stream of a particular
show (eg. in a launcher/alarm clock setup).

## Usage

    python oe1.py [-d DATE] [-f FILTER] [-h] [-r] [-u]

### Arguments

The following arguments are available:

| Arguments                  |                                               |
| -------------------------- | --------------------------------------------- |
| -d *DATE*, --date *DATE*       | Obtain program items for *DATE*.       |
| -f *FILTER*, --filter *FILTER* | Filter program elements by the string *FILTER*. |
| -h, --help                 | Show help message and exit.                   |
| -r, --reverse              | Reverse results.                              |
| -u, --url                  | Only Print URL(s) of matching program items.  |

## Examples

### Get radio program for today

    $ python oe1.py
    Program for 20160430:

    Time                          Title                                               Info
    06:00                    Nachrichten                                                   
    06:05        Guten Morgen Österreich  Klassik trifft auf Jazz. Zu Beginn des Ö1-Jazz...
    06:56           Gedanken für den Tag  von Oliver Tanzer, Autor und Leiter des Wirtsc...
    07:00              Morgenjournal (I)  BP-Wahl: Kritik an Meinungsforschern und Medie...
    07:33        Guten Morgen Österreich  Klassik trifft auf Jazz: Zu Beginn des Ö1-Jazz...
    07:55                  Schon gehört?  Die Ö1 Club-Sendung. Aktuelle Veranstaltungen ...
    08:00             Morgenjournal (II)  Italien: Kontrollen in Zügen wieder erlaubt / ...

### Get radio program for the previous day

    $ python oe1.py -d -1
    Program for 20160429:

    Time                                    Title                                               Info
    05:00                              Nachrichten                                                   
    05:03                  Guten Morgen Österreich  Präsentation: Bernhard Eppensteiner; Musikausw...
    06:00                              Frühjournal                                                   
     ...                                       ...  ...
    00:05                        Zeit-Ton extended  (Fortsetzung). Zeit-Ton extended. Die neue Hip...
    02:00                              Nachrichten                                                   
    02:03                      Die Ö1 Klassiknacht  Präsentation: Michael Köppel; Musikauswahl: Ge...

### Get radio program for today and print it in reverse order

    $ python oe1.py
    Program for 20160430:

    Time                          Title                                               Info
    08:00             Morgenjournal (II)  Italien: Kontrollen in Zügen wieder erlaubt / ...
    07:55                  Schon gehört?  Die Ö1 Club-Sendung. Aktuelle Veranstaltungen ...
    07:33        Guten Morgen Österreich  Klassik trifft auf Jazz: Zu Beginn des Ö1-Jazz...
    07:00              Morgenjournal (I)  BP-Wahl: Kritik an Meinungsforschern und Medie...
    06:56           Gedanken für den Tag  von Oliver Tanzer, Autor und Leiter des Wirtsc...
    06:05        Guten Morgen Österreich  Klassik trifft auf Jazz. Zu Beginn des Ö1-Jazz...
    06:00                    Nachrichten                                                   

### Filter the radio program for a particular show

    $ python oe1.py -f Morgenjournal
    Program for 20160430:

    Time                          Title                                               Info
    07:00              Morgenjournal (I)  BP-Wahl: Kritik an Meinungsforschern und Medie...
    08:00             Morgenjournal (II)  Italien: Kontrollen in Zügen wieder erlaubt / ...

### Filter the radio program and print the URL for the stream

    $ python oe1.py -f Morgenjournal -u
    http://loopstream01.apa.at/?channel=oe1&id=20160430_0700_6_1_journal_XXX_w_

The -u argument is particularly useful in combination with ```[xargs][1]```/```[open][2]```:

    $ python oe1.py -f Morgenjournal -u | xargs open

[1]: https://en.wikipedia.org/wiki/Xargs
[2]: https://webcache.googleusercontent.com/search?q=cache:QTJqLb2_BVoJ:https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man1/open.1.html+&cd=1&hl=en&ct=clnk&gl=uk
