def Countdown(Time):
    import time
    _ = Time
    o_ = 0
    while _ > 0:
        print(_, " ", end="")
        _ -= 1
        o_ += 1
        time.sleep(1)
        if o_ > 10:
            print()
            o_ = 0
    print()