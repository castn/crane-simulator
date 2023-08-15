#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <KXmlGuiWindow>
#include "src/view/CentralWidget.h"
#include "src/crane/crane.h"

class KTextEdit;
class KJob;
class CentralWidget;

class MainWindow : public KXmlGuiWindow {
Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    void openFileFromUrl(const QUrl &inputFileName);
private:
    Crane *crane = nullptr;

    void setupActions();
    void saveFileToDisk(const QString &outputFileName);

    KTextEdit *textArea;
    QString fileName;
    CentralWidget *mainWidget = nullptr;

    QWidget *createCentralWidget();
private Q_SLOTS:
    void newFile();
    void openFile();
    void saveFile();
    void saveFileAs();
    void downloadFinished(KJob *job);
public slots:
    void handleApply();
};

#endif // MAINWINDOW_H