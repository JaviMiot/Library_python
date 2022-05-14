class Aritmetic:
    def sum(self):
        pass


def test_mockup(monkeypatch):
    def mockup_test():
        def sum():
            return 4 + 5
        return sum()

    monkeypatch.setattr(Aritmetic, 'sum', mockup_test)

    a = Aritmetic()
    assert a.sum() == 9
