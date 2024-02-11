from WeatherFetcher import WeatherFetcher
import PySimpleGUI as sg

def main():
    weatherFeather = WeatherFetcher()
    layout = [[sg.Text("Can I Bike Today?")], [sg.Button("Check")]]
    window = sg.Window('Can I Bike Today?', layout, margins=(400, 200))

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window. 
        if event == sg.WINDOW_CLOSED:
            break
        if event == "Check":
            match weatherFeather.CheckRainLastThreeDays():
                case False:
                    print("ITS BIKING TIME BAYBEEEEE")
                case True:
                    print("Nah, fuck you lol")
                

    window.close()



if __name__ == "__main__":
    main()
    
    # while(True) {
    # }
# End of file (EOF)