# myapp/forms.py

from django import forms

class ParticipationForm(forms.Form):
    name = forms.CharField(max_length=100) 
    email = forms.EmailField()
    organisation = forms.CharField(max_length=200)
    rollno = forms.CharField(max_length=20)

class RatingForm1(forms.Form):
    error_description_11 = forms.ChoiceField(
        choices=[('The program prints "s" instead of "sum" and uses the wrong loop condition, excluding the nth triangle number.', 'The program prints "s" instead of "sum" and uses the wrong loop condition, excluding the nth triangle number.'), 
                 ('The variable sum is incorrectly initialized outside the loop, causing potential undefined behavior and inaccurate summation.', 'The variable sum is incorrectly initialized outside the loop, causing potential undefined behavior and inaccurate summation.'),
                 ('The formula used to calculate s inside the loop is incorrect, missing the term i + 2, which leads to wrong summation values.', 'The formula used to calculate s inside the loop is incorrect, missing the term i + 2, which leads to wrong summation values.')],
        widget=forms.RadioSelect,
        label="Select from the following options that best describe the error in the given program:"
    )
    understandability11 = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How difficult is it to identify the logical error(s) in the given program?")
    error_description_12 = forms.ChoiceField(
        choices=[('The program prints "s" instead of "sum" and uses the wrong loop condition, excluding the nth triangle number.', 'The program prints "s" instead of "sum" and uses the wrong loop condition, excluding the nth triangle number.'), 
                 ('The variable sum is incorrectly initialized outside the loop, causing potential undefined behavior and inaccurate summation.', 'The variable sum is incorrectly initialized outside the loop, causing potential undefined behavior and inaccurate summation.'),
                 ('The formula used to calculate s inside the loop is incorrect, missing the term i + 2, which leads to wrong summation values.', 'The formula used to calculate s inside the loop is incorrect, missing the term i + 2, which leads to wrong summation values.')],
        widget=forms.RadioSelect,
        required=True,
        label="Select from the following options that best describe the error in the given program:"
    )
    understandability12 = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")

class RatingForm2(forms.Form):
    error_description_21 = forms.ChoiceField(
        choices=[('The program\'s off-by-one error in the sorting loop causes incorrect side ordering, leading to wrong triangle classifications.', 'The program\'s off-by-one error in the sorting loop causes incorrect side ordering, leading to wrong triangle classifications.'),
                 ('The program\'s invalid triangle check fails for cases like \"1 2 3\" due to a missing equality operator in the condition.', 'The program\'s invalid triangle check fails for cases like \"1 2 3\" due to a missing equality operator in the condition.'), 
                 ('The program misuses triangle classification conditions, leading to incorrect outputs, particularly in distinguishing acute from obtuse triangles.', 'The program misuses triangle classification conditions, leading to incorrect outputs, particularly in distinguishing acute from obtuse triangles.')],
        widget=forms.RadioSelect,
        label="Select from the following options that best describe the error in the given program:"
    )
    understandability21 = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How difficult is it to identify the logical error(s) in the given program?")
    error_description_22 = forms.ChoiceField(
        choices=[('The program\'s off-by-one error in the sorting loop causes incorrect side ordering, leading to wrong triangle classifications.', 'The program\'s off-by-one error in the sorting loop causes incorrect side ordering, leading to wrong triangle classifications.'),
                 ('The program\'s invalid triangle check fails for cases like \"1 2 3\" due to a missing equality operator in the condition.', 'The program\'s invalid triangle check fails for cases like \"1 2 3\" due to a missing equality operator in the condition.'), 
                 ('The program misuses triangle classification conditions, leading to incorrect outputs, particularly in distinguishing acute from obtuse triangles.', 'The program misuses triangle classification conditions, leading to incorrect outputs, particularly in distinguishing acute from obtuse triangles.')],
        widget=forms.RadioSelect,
        required=True,
        label="Select from the following options that best describe the error in the given program:"
    )
    understandability22 = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")

class RatingForm3(forms.Form):
    error_description_31 = forms.ChoiceField(
        choices=[('The check_prime function fails to handle edge cases for numbers less than 2, leading to incorrect results.', 'The check_prime function fails to handle edge cases for numbers less than 2, leading to incorrect results.'),
                 ('The program risks out-of-range access near N by not checking the upper bound in the check_prime(i + 2) call.', 'The program risks out-of-range access near N by not checking the upper bound in the check_prime(i + 2) call.'),
                 ('The check_prime function inaccurately identifies primes and needs a more efficient method while properly handling edge cases.', 'The check_prime function inaccurately identifies primes and needs a more efficient method while properly handling edge cases.')],
        widget=forms.RadioSelect,
        label="Select from the following options that best describe the error in the given program:"
    )
    understandability31 = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How difficult is it to identify the logical error(s) in the given program?")
    error_description_32 = forms.ChoiceField(
        choices=[('The check_prime function fails to handle edge cases for numbers less than 2, leading to incorrect results.', 'The check_prime function fails to handle edge cases for numbers less than 2, leading to incorrect results.'),
                 ('The program risks out-of-range access near N by not checking the upper bound in the check_prime(i + 2) call.', 'The program risks out-of-range access near N by not checking the upper bound in the check_prime(i + 2) call.'),
                 ('The check_prime function inaccurately identifies primes and needs a more efficient method while properly handling edge cases.', 'The check_prime function inaccurately identifies primes and needs a more efficient method while properly handling edge cases.')],
        widget=forms.RadioSelect,
        required=True,
        label="Select from the following options that best describe the error in the given program:"
    )
    understandability32 = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    
class RatingForm4(forms.Form):
    error_description_41 = forms.ChoiceField(
        choices=[('The \'check_prime\' function lacks a condition to handle the edge case of `num=1` which is not a prime number.', 'The \'check_prime\' function lacks a condition to handle the edge case of `num=1` which is not a prime number.'),
                ('The boundary condition in the check_prime function is incorrect. The loop should run while j <= sqrt(num) instead of j <= num - 1.', 'The boundary condition in the check_prime function is incorrect. The loop should run while j <= sqrt(num) instead of j <= num - 1.'),
                ('The main function\'s loop starts with i = N and checks prime numbers without changing i, causing it to never exit the loop for non-prime inputs.', 'The main function\'s loop starts with i = N and checks prime numbers without changing i, causing it to never exit the loop for non-prime inputs.')],
        widget=forms.RadioSelect,
        label="Select from the following options that best describe the error in the given program:"
    )
    understandability41 = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How difficult is it to identify the logical error(s) in the given program?")
    error_description_42 = forms.ChoiceField(
        choices=[('The \'check_prime\' function lacks a condition to handle the edge case of `num=1` which is not a prime number.', 'The \'check_prime\' function lacks a condition to handle the edge case of `num=1` which is not a prime number.'),
                ('The boundary condition in the check_prime function is incorrect. The loop should run while j <= sqrt(num) instead of j <= num - 1.', 'The boundary condition in the check_prime function is incorrect. The loop should run while j <= sqrt(num) instead of j <= num - 1.'),
                ('The main function\'s loop starts with i = N and checks prime numbers without changing i, causing it to never exit the loop for non-prime inputs.', 'The main function\'s loop starts with i = N and checks prime numbers without changing i, causing it to never exit the loop for non-prime inputs.')],
        widget=forms.RadioSelect,
        required=True,
        label="Select from the following options that best describe the error in the given program:"
    )
    understandability42 = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    
class RatingForm5(forms.Form):
    error_description_51 = forms.ChoiceField(
        choices=[('The check_prime function mishandles num == 1 and fails to identify primes above 3 due to a flawed num_divisors approach.', 'The check_prime function mishandles num == 1 and fails to identify primes above 3 due to a flawed num_divisors approach.'), 
                 ('The main function\'s do-while loop risks running indefinitely if check_prime fails, requiring proper edge case handling and prime number incrementing.', 'The main function\'s do-while loop risks running indefinitely if check_prime fails, requiring proper edge case handling and prime number incrementing.'),
                 ('The boundary condition in the for loop should be i <= (int)sqrt(num) instead of i < (int)sqrt(num) to correctly identify prime numbers.', 'The boundary condition in the for loop should be i <= (int)sqrt(num) instead of i < (int)sqrt(num) to correctly identify prime numbers.')],
        widget=forms.RadioSelect,
        label="Select from the following options that best describe the error in the given program:"
    )
    understandability51 = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How difficult is it to identify the logical error(s) in the given program?")
    error_description_52 = forms.ChoiceField(
        choices=[('The check_prime function mishandles num == 1 and fails to identify primes above 3 due to a flawed num_divisors approach.', 'The check_prime function mishandles num == 1 and fails to identify primes above 3 due to a flawed num_divisors approach.'), 
                 ('The main function\'s do-while loop risks running indefinitely if check_prime fails, requiring proper edge case handling and prime number incrementing.', 'The main function\'s do-while loop risks running indefinitely if check_prime fails, requiring proper edge case handling and prime number incrementing.'),
                 ('The boundary condition in the for loop should be i <= (int)sqrt(num) instead of i < (int)sqrt(num) to correctly identify prime numbers.', 'The boundary condition in the for loop should be i <= (int)sqrt(num) instead of i < (int)sqrt(num) to correctly identify prime numbers.')],
        widget=forms.RadioSelect,
        required=True,
        label="Select from the following options that best describe the error in the given program:"
    )
    understandability52 = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    
class RatingForm6(forms.Form):
    error_description_61 = forms.ChoiceField(
        choices=[('The duplicate function\'s comparison approach causes repeated counts of the same duplicates, requiring a new method to handle multiple duplicates correctly.', 'The duplicate function\'s comparison approach causes repeated counts of the same duplicates, requiring a new method to handle multiple duplicates correctly.'), 
                 ('The duplicate function fails to detect duplicates in the first two elements due to incorrect iteration, and the inner loop should start at k + 1 to prevent redundant comparisons.', 'The duplicate function fails to detect duplicates in the first two elements due to incorrect iteration, and the inner loop should start at k + 1 to prevent redundant comparisons.'),
                 ('The main function lacks checks for edge cases with empty or single-element arrays, risking errors in the duplicate function for minimal input sizes.', 'The main function lacks checks for edge cases with empty or single-element arrays, risking errors in the duplicate function for minimal input sizes.')],
        
        widget=forms.RadioSelect,
        label="Select from the following options that best describe the error in the given program:"
    )
    understandability61 = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How difficult is it to identify the logical error(s) in the given program?")
    error_description_62 = forms.ChoiceField(
        choices=[('The duplicate function\'s comparison approach causes repeated counts of the same duplicates, requiring a new method to handle multiple duplicates correctly.', 'The duplicate function\'s comparison approach causes repeated counts of the same duplicates, requiring a new method to handle multiple duplicates correctly.'), 
                 ('The duplicate function fails to detect duplicates in the first two elements due to incorrect iteration, and the inner loop should start at k + 1 to prevent redundant comparisons.', 'The duplicate function fails to detect duplicates in the first two elements due to incorrect iteration, and the inner loop should start at k + 1 to prevent redundant comparisons.'),
                 ('The main function lacks checks for edge cases with empty or single-element arrays, risking errors in the duplicate function for minimal input sizes.', 'The main function lacks checks for edge cases with empty or single-element arrays, risking errors in the duplicate function for minimal input sizes.')],
        widget=forms.RadioSelect,
        required=True,
        label="Select from the following options that best describe the error in the given program:"
    )
    understandability62 = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    
class RatingForm7(forms.Form):
    error_description_71 = forms.ChoiceField(
        choices=[('The viper function\'s incorrect use of < instead of <= causes failure for multiples of 5, preventing proper recursion termination when b reaches 0 or negative.', 'The viper function\'s incorrect use of < instead of <= causes failure for multiples of 5, preventing proper recursion termination when b reaches 0 or negative.'), 
                 ('The flawed interaction between viper and mountain functions causes an incorrect pattern, as the mountain function starts from an improperly derived value from viper without proper linkage.', 'The flawed interaction between viper and mountain functions causes an incorrect pattern, as the mountain function starts from an improperly derived value from viper without proper linkage.'),
                 ('The mountain function lacks proper boundary checks, leading to infinite recursion and potential stack overflow for input values where n is not a multiple of 5.', 'The mountain function lacks proper boundary checks, leading to infinite recursion and potential stack overflow for input values where n is not a multiple of 5.')],
        widget=forms.RadioSelect,
        label="Select from the following options that best describe the error in the given program:"
    )
    understandability71 = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How difficult is it to identify the logical error(s) in the given program?")
    error_description_72 = forms.ChoiceField(
        choices=[('The viper function\'s incorrect use of < instead of <= causes failure for multiples of 5, preventing proper recursion termination when b reaches 0 or negative.', 'The viper function\'s incorrect use of < instead of <= causes failure for multiples of 5, preventing proper recursion termination when b reaches 0 or negative.'), 
                 ('The flawed interaction between viper and mountain functions causes an incorrect pattern, as the mountain function starts from an improperly derived value from viper without proper linkage.', 'The flawed interaction between viper and mountain functions causes an incorrect pattern, as the mountain function starts from an improperly derived value from viper without proper linkage.'),
                 ('The mountain function lacks proper boundary checks, leading to infinite recursion and potential stack overflow for input values where n is not a multiple of 5.', 'The mountain function lacks proper boundary checks, leading to infinite recursion and potential stack overflow for input values where n is not a multiple of 5.')],
        widget=forms.RadioSelect,
        required=True,
        label="Select from the following options that best describe the error in the given program:"
    )
    understandability72 = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")

class TARatingForm1(forms.Form):
    feedback11_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback12_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback13_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback14_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback15_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback16_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback17_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    
class TARatingForm2(forms.Form):
    feedback21_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback22_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback23_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback24_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback25_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback26_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback27_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    
class TARatingForm3(forms.Form):
    feedback31_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback32_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback33_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback34_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback35_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback36_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback37_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    
class TARatingForm4(forms.Form):
    feedback41_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback42_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback43_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback44_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback45_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback46_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback47_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")

    
class TARatingForm5(forms.Form):
    feedback51_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback52_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback53_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback54_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback55_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback56_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback57_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    
class TARatingForm6(forms.Form):
    feedback61_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback62_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback63_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback64_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback65_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback66_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback67_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    
class TARatingForm7(forms.Form):
    feedback71_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback72_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback73_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback74_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback75_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback76_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    feedback77_rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.HiddenInput(), label="How helpful is the feedback to understand the logical error(s) in the given program?")
    
class TAFeedbackForm1(forms.Form):
    ta_feedback1 = forms.CharField(
        label='Please provide an appropriate feedback that can help students to identify the logical error(s) in the given program.',
        max_length=5000,
        widget=forms.Textarea(attrs={
            'class': 'styled-textbox',
            'rows': 5,  
            'cols': 50, 
            'wrap': 'soft' 
        }),
        required=True,
    )
    
class TAFeedbackForm2(forms.Form):
    ta_feedback2 = forms.CharField(
        label='Please provide an appropriate feedback that can help students to identify the logical error(s) in the given program.',
        max_length=5000,
        widget=forms.Textarea(attrs={
            'class': 'styled-textbox',
            'rows': 5,  
            'cols': 50, 
            'wrap': 'soft' 
        }),
        required=True,
    )
    
class TAFeedbackForm3(forms.Form):
    ta_feedback3 = forms.CharField(
        label='Please provide an appropriate feedback that can help students to identify the logical error(s) in the given program.',
        max_length=5000,
        widget=forms.Textarea(attrs={
            'class': 'styled-textbox',
            'rows': 5,  
            'cols': 50, 
            'wrap': 'soft' 
        }),
        required=True,
    )
    
class TAFeedbackForm4(forms.Form):
    ta_feedback4 = forms.CharField(
        label='Please provide an appropriate feedback that can help students to identify the logical error(s) in the given program.',
        max_length=5000,
        widget=forms.Textarea(attrs={
            'class': 'styled-textbox',
            'rows': 5,  
            'cols': 50, 
            'wrap': 'soft' 
        }),
        required=True,
    )
    
class TAFeedbackForm5(forms.Form):
    ta_feedback5 = forms.CharField(
        label='Please provide an appropriate feedback that can help students to identify the logical error(s) in the given program.',
        max_length=5000,
        widget=forms.Textarea(attrs={
            'class': 'styled-textbox',
            'rows': 5,  
            'cols': 50, 
            'wrap': 'soft' 
        }),
        required=True,
    )
    
class TAFeedbackForm6(forms.Form):
    ta_feedback6 = forms.CharField(
        label='Please provide an appropriate feedback that can help students to identify the logical error(s) in the given program.',
        max_length=5000,
        widget=forms.Textarea(attrs={
            'class': 'styled-textbox',
            'rows': 5,  
            'cols': 50, 
            'wrap': 'soft' 
        }),
        required=True,
    )
    
class TAFeedbackForm7(forms.Form):
    ta_feedback7 = forms.CharField(
        label='Please provide an appropriate feedback that can help students to identify the logical error(s) in the given program.',
        max_length=5000,
        widget=forms.Textarea(attrs={
            'class': 'styled-textbox',
            'rows': 5,  
            'cols': 50, 
            'wrap': 'soft' 
        }),
        required=True,
    )