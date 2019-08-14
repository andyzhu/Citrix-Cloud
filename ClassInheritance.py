class LogicGate:

    def __init__(self, label):
        self.label = label
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performgatelogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self, label):
        LogicGate.__init__(self, label)

        self.PinA = None
        self.PinB = None

    def getPinA(self):
        return int(input("Enter Pin A input for the Gate" + self.getLabel()+"-->"))

    def getPinB(self):
        return int(input("Enter Pin B input for the Gate" + self.getLabel() + "-->"))


class UnaryGate(LogicGate):

    def __init__(self, label):
        LogicGate.__init__(self, label)

        self.pin = None

    def getPin(self):
        return int(input("Enter Pin A input for the Gate" + self.getLabel()+"-->"))


class AndGate(BinaryGate):

    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def performgatelogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):

    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def performgatelogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 0 and b == 0:
            return 0
        else:
            return 1


class NotGate(UnaryGate):

    def __init__(self, label):
        UnaryGate.__init__(self, label)

    def performgatelogic(self):
        a = self.getPin()

        if a == 0:
            return 0
        else:
            return 1


class Connector():
    def __init__(self, fromgate, togate):
        self.fromGate = fromgate
        self.toGate = togate

        togate.setNextPin(self)

    def getFrom(self):
        return self.fromGate

    def getTo(self):
        return self.toGate
