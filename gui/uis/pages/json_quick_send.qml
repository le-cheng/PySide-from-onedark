import QtQuick 2.15
import QtQml.Models 2.15

Rectangle {
    width: 300
    height: 300
    radius: 10

    signal updateSignal()

    gradient: Gradient {
        GradientStop { position: 0.0; color: "#dbddde" }
        GradientStop { position: 1.0; color: "#5fc9f8" }
    }

    ListModel {
        id: theModel

        ListElement { number: 0 }
        ListElement { number: 1 }
        ListElement { number: 2 }
        ListElement { number: 3 }
        ListElement { number: 4 }
        ListElement { number: 5 }
        ListElement { number: 6 }
        ListElement { number: 7 }
        ListElement { number: 8 }
        ListElement { number: 9 }
    }

    Rectangle {
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.margins: 3
        radius: 10

        height: 40

        color: "#53d769"
        border.color: Qt.lighter(color, 1.1)

        Text {
            anchors.centerIn: parent
            text: "Add item!"
        }

        MouseArea {
            anchors.fill: parent
            onClicked: {
                theModel.append({"number": ++parent.count});
                updateSignal()
            }
        }

        property int count: 9
    }

    ListView {
        anchors.fill: parent
        anchors.margins: 3
        anchors.bottomMargin: 80
        clip: true
        spacing: 5


        model: theModel
        delegate: numberDelegate
    }

    Component {
        id: numberDelegate

        Rectangle {
            id: wrapper
            width: 140
            height: 40
            radius: 10
            gradient: Gradient {
                GradientStop { position: 0.0; color: "#f8306a" }
                GradientStop { position: 1.0; color: "#fb5b40" }
            }

            Text {
                anchors.centerIn: parent
                font.pixelSize: 10
                text: number
            }

            MouseArea {
                anchors.fill: parent
                onClicked: {
                    theModel.remove(index);
                }
            }

            ListView.onRemove:remove_animation.start()
            ListView.onAdd:add_animation.start()

            // Animations
            // SequentialAnimation on state {
            //     id: wrapper2
            SequentialAnimation {
                id: remove_animation
                PropertyAction { target: wrapper; property: "ListView.delayRemove"; value: true }
                NumberAnimation {
                    target: wrapper;
                    property: "scale";
                    to: 0;
                    duration: 250;
                    easing.type: Easing.InOutBack
                }
                PropertyAction { target: wrapper; property: "ListView.delayRemove"; value: false }
            }

            SequentialAnimation {
                id: add_animation
                NumberAnimation { target: wrapper; property: "scale"; from: 0; to: 1; duration: 250; easing.type: Easing.InOutBack }
            }
            // }
        }
    }
}