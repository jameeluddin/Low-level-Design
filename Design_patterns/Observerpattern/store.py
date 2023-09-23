from Design_patterns.Observerpattern.Observable.IphoneObervableImpl import IphoneObservable
from Design_patterns.Observerpattern.Observer.EmailAlertObserverImpl import EmailAlertObserverImpl


def main():
    iphoneStockObservable = IphoneObservable()

    observer1 = EmailAlertObserverImpl("qwerty1@gmail.com", iphoneStockObservable)
    observer2 = EmailAlertObserverImpl("qwerty2@gmail.com", iphoneStockObservable)
    observer3 = EmailAlertObserverImpl("ecommerce user", iphoneStockObservable)

    iphoneStockObservable.add(observer1)
    iphoneStockObservable.add(observer2)
    iphoneStockObservable.add(observer3)

    iphoneStockObservable.set_stock_count(10)
    iphoneStockObservable.set_stock_count_to_zero()
    iphoneStockObservable.set_stock_count(100)


if __name__ == "__main__":
    main()
