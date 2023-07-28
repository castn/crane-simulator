#include <QApplication>
#include <QCommandLineParser>
#include <QDir>
#include <QUrl>
#include <KAboutData>
#include <KLocalizedString>
#include "mainwindow.h"

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);
    KAboutData aboutData(
            QStringLiteral("mainwindow"),
            i18n("Crane Simulator"),
            QStringLiteral("1.0.0"),
            i18n("A simple text area"),
            KAboutLicense::GPL_V3,
            i18n("Copyright 2023, authors of Crane Simulator"),
            i18n("<b>Crane Simulator 2024</b><br> is a software written in Python which was developed in the context of a project course at the TU Darmstadt. The source code is available on Github."),
            QStringLiteral("https://github.com/castn/crane-simulator"),
            QStringLiteral("submit@bugs.kde.org"));
    KLocalizedString::setApplicationDomain("mainwindow");


    aboutData.addAuthor(i18n("castn"), i18n("Maintainer"),
                        QStringLiteral("carsten.wesp@online.de"),
                        QStringLiteral("https://github.com/castn"));

    KAboutData::setApplicationData(aboutData);

    QCommandLineParser parser;
    parser.addPositionalArgument(QStringLiteral("file"), i18n("Document to open"));
    aboutData.setupCommandLine(&parser);
    aboutData.processCommandLine(&parser);


    parser.process(app);
    aboutData.processCommandLine(&parser);

    auto *window = new MainWindow();
    window->show();

    if (parser.positionalArguments().count() > 0) {
        window->openFileFromUrl(QUrl::fromUserInput(
                parser.positionalArguments().at(0),
                QDir::currentPath()));
    }


    return QApplication::exec();
}
