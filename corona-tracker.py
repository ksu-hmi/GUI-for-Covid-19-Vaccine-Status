# ===================================================== Importing libraries ===============================================
import covid                               # pip install covid
import tkinter as tk
import matplotlib.pyplot as plt            # pip install matplotlib
import pandas as pd                        # pip install pandas

#======================================================== End ===============================================================

# ===================================================== defining function that generate status =======================================
def show_data():
    data = covid.Covid()
    country_name = e1.get()
    status = data.get_status_by_country_name(country_name)
    Vaccinated = status['Vaccinated']
    e2.insert(0,list_of_doses_received)
    death = status['Partially Vaccinated']
    e3.insert(0, vaccine_name_with_the_dose_number)
    confirm = status['Not Vaccinated']
    e4.insert(0, patient_is_not_vaccinated/need_vaccine)
    print(status)
    # intialise data of lists.
    data = {'id': status['id'],
            'Patient_last_name': status['Patient_last_name'],
            'Patient_last_name': status['Patient_last_name'],
            'vaccinated': status['receviedbooster'],
            'partiallyvaccinated': status['partiallyvaccinated'],
            'notvaccinated': status['notvaccinated'],
            'Latitude': status['latitude'],
            'Longitude': status['longitude'],
            'Last_Updated': status['last_update']
            }

    # Create DataFrame
    df = pd.DataFrame(data, index=[0])

    # Print the output.
    print(df)
    cadr = {

        key:status[key]
        for key in status.keys() & {"Received Booster","Partially Vaccinated","Not Vaccinated"}
    }
    n = list(cadr.keys())
    v = list(cadr.values())
    plt.title("Patient Name")
    plt.bar(range(len(cadr)),v,tick_label=n,label=('Received Booster'))
    plt.xlabel('x-labels')
    plt.ylabel('data')

    plt.plot(range(len(cadr)))


    plt.show()

#============================================================== End ======================================================


# ================================================= Window Design =========================================================
master = tk.Tk()
master.title('Covid-19 Vaccine Status ')

tk.Label(master,text="COVID-19 VACCINE STATUS" ,padx=50).grid(row=0)


tk.Label(master, text="Enter patient's last name : -").grid(row=2)

e1 = tk.Entry(master)

e1.grid(row=2, column=3)

tk.Label(master, text="Enter patient's first name : -").grid(row=3)

e1 = tk.Entry(master)

e1.grid(row=3, column=3)

tk.Label(master, text="Enter patient's date of Birth : -").grid(row=4)

e1 = tk.Entry(master)

e1.grid(row=4, column=3)

tk.Button(master, text='OR').grid(row=6)

tk.Label(master, text="Enter patient's MRN : -").grid(row=7)

e1 = tk.Entry(master)

e1.grid(row=7, column=3)

tk.Button(master,
          text='Show', command=show_data).grid(row=9,
                                                       column=3,
                                                       sticky=tk.W,
                                                       pady=4)


tk.Label(master, text="Vaccinated : -").grid(row=11)

e2 = tk.Entry(master)
e2.grid(row=11, column=3)

tk.Label(master, text="Partially Vaccinated : -").grid(row=12)
e3 = tk.Entry(master)
e3.grid(row=12, column=3)

tk.Label(master, text="Not Vaccinated : -").grid(row=13)
e4 = tk.Entry(master)
e4.grid(row=13, column=3)


master.mainloop()

#================================================================== End =====================================================

