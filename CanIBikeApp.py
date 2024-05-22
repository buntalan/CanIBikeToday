from WeatherFetcher import WeatherFetcher
import PySimpleGUI as sg

def main():
    # Call istance of WeatherFetcher
    weatherFeather = WeatherFetcher()

    # Initialize window elements
    button = sg.Button("Check")
    layout = [[sg.Text("Can I Bike Today?", key='status')], [button]]
    window = sg.Window('Can I Bike Today?', 
                       layout, 
                       margins=(400, 200), 
                       finalize=True)

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window. 
        if event == sg.WINDOW_CLOSED:
            break
        if event == "Check":
            match weatherFeather.CheckRainLastThreeDays():
                case False:
                    window['status'].update('Time to bike!')
                case True:
                    window['status'].update('Not today... Check tomorrow!')
                
    window.close()


if __name__ == "__main__":
    main()
    
    # while(True) {
    # }
# End of file (EOF)