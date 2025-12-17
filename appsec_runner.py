from engine.appsec_engine import AppSecEngine

if __name__ == "__main__":
    target = input("Enter target web URL: ")
    engine = AppSecEngine(target)
    engine.execute()
