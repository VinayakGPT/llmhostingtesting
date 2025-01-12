from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
 
from .forms import (
    ParticipationForm, RatingForm1, RatingForm2, RatingForm3, RatingForm4,
    RatingForm5, RatingForm6, RatingForm7, TARatingForm1, TARatingForm2,
    TARatingForm3, TARatingForm4, TARatingForm5, TARatingForm6, TARatingForm7, 
    TAFeedbackForm1, TAFeedbackForm2, TAFeedbackForm3, TAFeedbackForm4,
    TAFeedbackForm5, TAFeedbackForm6, TAFeedbackForm7
)
from .models import Phase, UserSubmission, TASubmission, TAFeedback, Feedback

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_control_panel')
        else:
            messages.error(request, "Invalid credentials or unauthorized access.")
    return render(request, 'admin_login.html')

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render

@login_required
def admin_control_panel(request):
    if not request.user.is_staff:
        return redirect('index')

    # Get all phases from the database
    phases = Phase.objects.all()

    # Get the active phase
    active_phase = Phase.objects.filter(is_active=True).first()

    if request.method == 'POST':
        # Check if the "Show Demo" button was clicked
        if 'show_demo' in request.POST:
            # Redirect to the demo URL of the currently active phase
            if active_phase:
                if active_phase.name == 'Manual TA feedback':
                    return redirect('demo_phase1')
                elif active_phase.name == 'Feedback rating by TA':
                    return redirect('demo_phase2')
                elif active_phase.name == 'Feedback rating by Student':
                    return redirect('demo_phase3')
            else:
                messages.error(request, "No active phase to show demo.")
        else:
            # Handle "Update Phase" button click
            selected_phase_id = request.POST.get('selected_phase')
            if selected_phase_id:
                try:
                    selected_phase = Phase.objects.get(id=selected_phase_id)

                    # Deactivate all phases and activate the selected phase
                    Phase.objects.update(is_active=False)
                    selected_phase.is_active = True
                    selected_phase.save()

                    # Update active_phase immediately
                    active_phase = selected_phase

                    messages.success(request, f"Phase updated successfully.")
                except Phase.DoesNotExist:
                    messages.error(request, "The selected phase does not exist.")
            else:
                messages.error(request, "Please select a valid phase before updating.")

    context = {
        'active_phase': active_phase,
        'phases': phases
    }

    return render(request, 'admin_control_panel.html', context)

@login_required
def demo_phase1(request):
    return render(request, 'demo_phase1.html')

@login_required
def demo_phase2(request):
    return render(request, 'demo_phase2.html')

@login_required
def demo_phase3(request):
    return render(request, 'demo_phase3.html')

def participation_page(request):
    if request.method == 'POST':
        form = ParticipationForm(request.POST)
        if form.is_valid():
            # Store form data in the session
            request.session['participation_data'] = form.cleaned_data

            # Retrieve the active phase from the database
            active_phase_obj = Phase.objects.filter(is_active=True).first()  # Assuming only one active phase at a time
            if active_phase_obj:
                active_phase = active_phase_obj.name  # The name or identifier of the active phase
            else:
                active_phase = 'Manual TA feedback'  # Default phase if no active phase is found

            # Redirect based on the active phase
            if active_phase == 'Manual TA feedback':
                return redirect('ta_overview2')  # Phase 1 - Redirect to TA Overview 2
            elif active_phase == 'Feedback rating by TA':
                return redirect('ta_overview')   # Phase 2 - Redirect to TA Overview
            elif active_phase == 'Feedback rating by Student':
                return redirect('student_overview')  # Phase 3 - Redirect to Student Overview
    else:
        form = ParticipationForm()

    return render(request, 'participation_page.html', {'form': form})

def reset_visited_pages(request):
    request.session['visited_pages'] = [] 
    
def student_overview(request):
    return render(request, 'student_overview.html')

def problem1(request, page_number):
    
    visited_pages = request.session.get('visited_pages', [])
    
    if page_number not in visited_pages:
        visited_pages.append(page_number)
        request.session['visited_pages'] = visited_pages
    
    if request.method == 'POST':
        form = RatingForm1(request.POST)
        if form.is_valid():
            request.session['rating1_data'] = form.cleaned_data
            request.session['understandability11'] = form.cleaned_data.get('understandability11', 0)
            request.session['understandability12'] = form.cleaned_data.get('understandability12', 0)
            return redirect('problem2', page_number=page_number + 1)
    else:
        initial_data = {
            'error_description_11': request.session.get('rating1_data', {}).get('error_description_11', ''),
            'understandability11': request.session.get('rating1_data', {}).get('understandability11', ''),
            'error_description_12': request.session.get('rating1_data', {}).get('error_description_12', ''),
            'understandability12': request.session.get('rating1_data', {}).get('understandability12', ''),
        }
        form = RatingForm1(initial=initial_data)
    understandability = {f'understandability1{i}': request.session.get(f'understandability1{i}', 0) for i in range(1, 3)}
    
    tasubmissions = TASubmission.objects.all()
    
    average_ratings = {
        'feedback11_rating': [],
        'feedback12_rating': [],
        'feedback13_rating': [],
        'feedback14_rating': [],
        'feedback15_rating': [],
        'feedback16_rating': [],
        'feedback17_rating': [],
    }
    
    for submission in tasubmissions:
        average_ratings['feedback11_rating'].append(submission.feedback11_rating)
        average_ratings['feedback12_rating'].append(submission.feedback12_rating)
        average_ratings['feedback13_rating'].append(submission.feedback13_rating)
        average_ratings['feedback14_rating'].append(submission.feedback14_rating)
        average_ratings['feedback15_rating'].append(submission.feedback15_rating)
        average_ratings['feedback16_rating'].append(submission.feedback16_rating)
        average_ratings['feedback17_rating'].append(submission.feedback17_rating)

    
    calculated_averages = {key: (sum(values) / len(values) if values else 0) for key, values in average_ratings.items()}

    highest_feedback_key = max(calculated_averages, key=calculated_averages.get)

    feedback_content_map = {
        'feedback11_rating': ('content1', 'Feedback 11'),
        'feedback12_rating': ('content2', 'Feedback 12'),
        'feedback13_rating': ('content3', 'Feedback 13'),
        'feedback14_rating': ('content4', 'Feedback 14'),
        'feedback15_rating': ('content5', 'Feedback 15'),
        'feedback16_rating': ('content6', 'Feedback 16'),
        'feedback17_rating': ('content7', 'Feedback 17'),
    }

    highest_content_field, highest_feedback_name = feedback_content_map[highest_feedback_key]

    # Retrieve the latest two TAFeedback entries
    latest_feedbacks = TAFeedback.objects.order_by('-id')[:2]
    ta_feedback_1 = latest_feedbacks[0] if len(latest_feedbacks) > 0 else None
    ta_feedback_2 = latest_feedbacks[1] if len(latest_feedbacks) > 1 else None

    if highest_feedback_key == 'feedback16_rating':
        highest_rating_content = ta_feedback_1.ta_feedback1 if ta_feedback_1 else "No TA feedback available"
    elif highest_feedback_key == 'feedback17_rating':
        highest_rating_content = ta_feedback_2.ta_feedback1 if ta_feedback_2 else "No TA feedback available"
    else:
        highest_rated_feedback = Feedback.objects.filter(problem_id=1).first()

        if highest_rated_feedback:
            highest_rating_content = getattr(highest_rated_feedback, highest_content_field)  
        else:
            highest_rating_content = "No feedback available"

    context = {
        'form': form,
        'highest_rating_content': highest_rating_content,
        'highest_feedback_name': highest_feedback_name,
        'average_ratings': calculated_averages,
        'current_page': page_number,
        'understandability': understandability,
        'visited_pages': request.session['visited_pages'],
    }

    return render(request, 'problem1.html', context)


def problem2(request, page_number):
    
    visited_pages = request.session.get('visited_pages', [])
    
    if page_number not in visited_pages:
        visited_pages.append(page_number)
        request.session['visited_pages'] = visited_pages
    
    if request.method == 'POST':
        form = RatingForm2(request.POST)
        if form.is_valid():
            request.session['rating2_data'] = form.cleaned_data
            request.session['understandability21'] = form.cleaned_data.get('understandability21', 0)
            request.session['understandability22'] = form.cleaned_data.get('understandability22', 0)
            return redirect('problem3', page_number=page_number + 1)
    else:
        initial_data = {
            'error_description_21': request.session.get('rating2_data', {}).get('error_description_21', ''),
            'understandability21': request.session.get('rating2_data', {}).get('understandability21', ''),
            'error_description_22': request.session.get('rating2_data', {}).get('error_description_22', ''),
            'understandability22': request.session.get('rating2_data', {}).get('understandability22', ''),
        }
        form = RatingForm2(initial=initial_data)
    understandability = {f'understandability2{i}': request.session.get(f'understandability2{i}', 0) for i in range(1, 3)}

    tasubmissions = TASubmission.objects.all()

    average_ratings = {
        'feedback21_rating': [],
        'feedback22_rating': [],
        'feedback23_rating': [],
        'feedback24_rating': [],
        'feedback25_rating': [],
        'feedback26_rating': [],
        'feedback27_rating': [],
    }

    for submission in tasubmissions:
        average_ratings['feedback21_rating'].append(submission.feedback21_rating)
        average_ratings['feedback22_rating'].append(submission.feedback22_rating)
        average_ratings['feedback23_rating'].append(submission.feedback23_rating)
        average_ratings['feedback24_rating'].append(submission.feedback24_rating)
        average_ratings['feedback25_rating'].append(submission.feedback25_rating)
        average_ratings['feedback26_rating'].append(submission.feedback26_rating)
        average_ratings['feedback27_rating'].append(submission.feedback27_rating)

    calculated_averages = {key: (sum(values) / len(values) if values else 0) for key, values in average_ratings.items()}

    highest_feedback_key = max(calculated_averages, key=calculated_averages.get)

    feedback_content_map = {
        'feedback21_rating': ('content1', 'Feedback 21'),
        'feedback22_rating': ('content2', 'Feedback 22'),
        'feedback23_rating': ('content3', 'Feedback 23'),
        'feedback24_rating': ('content4', 'Feedback 24'),
        'feedback25_rating': ('content5', 'Feedback 25'),
        'feedback26_rating': ('content6', 'Feedback 26'),
        'feedback27_rating': ('content7', 'Feedback 27'),
    }

    highest_content_field, highest_feedback_name = feedback_content_map[highest_feedback_key]

    # Retrieve the latest two TAFeedback entries
    latest_feedbacks = TAFeedback.objects.order_by('-id')[:2]
    ta_feedback_1 = latest_feedbacks[0] if len(latest_feedbacks) > 0 else None
    ta_feedback_2 = latest_feedbacks[1] if len(latest_feedbacks) > 1 else None

    if highest_feedback_key == 'feedback26_rating':
        highest_rating_content = ta_feedback_1.ta_feedback2 if ta_feedback_1 else "No TA feedback available"
    elif highest_feedback_key == 'feedback27_rating':
        highest_rating_content = ta_feedback_2.ta_feedback2 if ta_feedback_2 else "No TA feedback available"
    else:
        highest_rated_feedback = Feedback.objects.filter(problem_id=2).first()

        if highest_rated_feedback:
            highest_rating_content = getattr(highest_rated_feedback, highest_content_field)  
        else:
            highest_rating_content = "No feedback available"

    context = {
        'form': form,
        'highest_rating_content': highest_rating_content,
        'highest_feedback_name': highest_feedback_name,
        'average_ratings': calculated_averages,
        'current_page': page_number,
        'understandability': understandability,
        'visited_pages': request.session['visited_pages'],
    }

    return render(request, 'problem2.html', context)


def problem3(request, page_number):
    
    visited_pages = request.session.get('visited_pages', [])
    
    if page_number not in visited_pages:
        visited_pages.append(page_number)
        request.session['visited_pages'] = visited_pages
    
    if request.method == 'POST':
        form = RatingForm3(request.POST)
        if form.is_valid():
            request.session['rating3_data'] = form.cleaned_data
            request.session['understandability31'] = form.cleaned_data.get('understandability31', 0)
            request.session['understandability32'] = form.cleaned_data.get('understandability32', 0)
            return redirect('problem4', page_number=page_number + 1)
    else:
        initial_data = {
            'error_description_31': request.session.get('rating3_data', {}).get('error_description_31', ''),
            'understandability31': request.session.get('rating3_data', {}).get('understandability31', ''),
            'error_description_32': request.session.get('rating3_data', {}).get('error_description_32', ''),
            'understandability32': request.session.get('rating3_data', {}).get('understandability32', ''),
        }
        form = RatingForm3(initial=initial_data)
    understandability = {f'understandability3{i}': request.session.get(f'understandability3{i}', 0) for i in range(1, 3)}

    tasubmissions = TASubmission.objects.all()

    average_ratings = {
        'feedback31_rating': [],
        'feedback32_rating': [],
        'feedback33_rating': [],
        'feedback34_rating': [],
        'feedback35_rating': [],
        'feedback36_rating': [],
        'feedback37_rating': [],
    }

    for submission in tasubmissions:
        average_ratings['feedback31_rating'].append(submission.feedback31_rating)
        average_ratings['feedback32_rating'].append(submission.feedback32_rating)
        average_ratings['feedback33_rating'].append(submission.feedback33_rating)
        average_ratings['feedback34_rating'].append(submission.feedback34_rating)
        average_ratings['feedback35_rating'].append(submission.feedback35_rating)
        average_ratings['feedback36_rating'].append(submission.feedback36_rating)
        average_ratings['feedback37_rating'].append(submission.feedback37_rating)

    calculated_averages = {key: (sum(values) / len(values) if values else 0) for key, values in average_ratings.items()}

    highest_feedback_key = max(calculated_averages, key=calculated_averages.get)

    feedback_content_map = {
        'feedback31_rating': ('content1', 'Feedback 31'),
        'feedback32_rating': ('content2', 'Feedback 32'),
        'feedback33_rating': ('content3', 'Feedback 33'),
        'feedback34_rating': ('content4', 'Feedback 34'),
        'feedback35_rating': ('content5', 'Feedback 35'),
        'feedback36_rating': ('content6', 'Feedback 36'),
        'feedback37_rating': ('content7', 'Feedback 37'),
    }

    highest_content_field, highest_feedback_name = feedback_content_map[highest_feedback_key]

    # Retrieve the latest two TAFeedback entries
    latest_feedbacks = TAFeedback.objects.order_by('-id')[:2]
    ta_feedback_1 = latest_feedbacks[0] if len(latest_feedbacks) > 0 else None
    ta_feedback_2 = latest_feedbacks[1] if len(latest_feedbacks) > 1 else None

    if highest_feedback_key == 'feedback36_rating':
        highest_rating_content = ta_feedback_1.ta_feedback3 if ta_feedback_1 else "No TA feedback available"
    elif highest_feedback_key == 'feedback37_rating':
        highest_rating_content = ta_feedback_2.ta_feedback3 if ta_feedback_2 else "No TA feedback available"
    else:
        highest_rated_feedback = Feedback.objects.filter(problem_id=3).first()

        if highest_rated_feedback:
            highest_rating_content = getattr(highest_rated_feedback, highest_content_field)  
        else:
            highest_rating_content = "No feedback available"

    context = {
        'form': form,
        'highest_rating_content': highest_rating_content,
        'highest_feedback_name': highest_feedback_name,
        'average_ratings': calculated_averages,
        'understandability': understandability,
        'current_page': page_number,
        'visited_pages': request.session['visited_pages'],
    }

    return render(request, 'problem3.html', context)


def problem4(request, page_number):
    
    visited_pages = request.session.get('visited_pages', [])
    
    if page_number not in visited_pages:
        visited_pages.append(page_number)
        request.session['visited_pages'] = visited_pages
    
    if request.method == 'POST':
        form = RatingForm4(request.POST)
        if form.is_valid():
            request.session['rating4_data'] = form.cleaned_data
            request.session['understandability41'] = form.cleaned_data.get('understandability41', 0)
            request.session['understandability42'] = form.cleaned_data.get('understandability42', 0)
            return redirect('problem5', page_number=page_number + 1)
    else:
        initial_data = {
            'error_description_41': request.session.get('rating4_data', {}).get('error_description_41', ''),
            'understandability41': request.session.get('rating4_data', {}).get('understandability41', ''),
            'error_description_42': request.session.get('rating4_data', {}).get('error_description_42', ''),
            'understandability42': request.session.get('rating4_data', {}).get('understandability42', ''),
        }
        form = RatingForm4(initial=initial_data)
    understandability = {f'understandability4{i}': request.session.get(f'understandability4{i}', 0) for i in range(1, 3)}

    tasubmissions = TASubmission.objects.all()

    average_ratings = {
        'feedback41_rating': [],
        'feedback42_rating': [],
        'feedback43_rating': [],
        'feedback44_rating': [],
        'feedback45_rating': [],
        'feedback46_rating': [],
        'feedback47_rating': [],
    }

    for submission in tasubmissions:
        average_ratings['feedback41_rating'].append(submission.feedback41_rating)
        average_ratings['feedback42_rating'].append(submission.feedback42_rating)
        average_ratings['feedback43_rating'].append(submission.feedback43_rating)
        average_ratings['feedback44_rating'].append(submission.feedback44_rating)
        average_ratings['feedback45_rating'].append(submission.feedback45_rating)
        average_ratings['feedback46_rating'].append(submission.feedback46_rating)
        average_ratings['feedback47_rating'].append(submission.feedback47_rating)

    calculated_averages = {key: (sum(values) / len(values) if values else 0) for key, values in average_ratings.items()}

    highest_feedback_key = max(calculated_averages, key=calculated_averages.get)

    feedback_content_map = {
        'feedback41_rating': ('content1', 'Feedback 41'),
        'feedback42_rating': ('content2', 'Feedback 42'),
        'feedback43_rating': ('content3', 'Feedback 43'),
        'feedback44_rating': ('content4', 'Feedback 44'),
        'feedback45_rating': ('content5', 'Feedback 45'),
        'feedback46_rating': ('content6', 'Feedback 46'),
        'feedback47_rating': ('content7', 'Feedback 47'),
    }

    highest_content_field, highest_feedback_name = feedback_content_map[highest_feedback_key]

    # Retrieve the latest two TAFeedback entries
    latest_feedbacks = TAFeedback.objects.order_by('-id')[:2]
    ta_feedback_1 = latest_feedbacks[0] if len(latest_feedbacks) > 0 else None
    ta_feedback_2 = latest_feedbacks[1] if len(latest_feedbacks) > 1 else None

    if highest_feedback_key == 'feedback46_rating':
        highest_rating_content = ta_feedback_1.ta_feedback4 if ta_feedback_1 else "No TA feedback available"
    elif highest_feedback_key == 'feedback47_rating':
        highest_rating_content = ta_feedback_2.ta_feedback4 if ta_feedback_2 else "No TA feedback available"
    else:
        highest_rated_feedback = Feedback.objects.filter(problem_id=4).first()

        if highest_rated_feedback:
            highest_rating_content = getattr(highest_rated_feedback, highest_content_field)  
        else:
            highest_rating_content = "No feedback available"

    context = {
        'form': form,
        'highest_rating_content': highest_rating_content,
        'highest_feedback_name': highest_feedback_name,
        'average_ratings': calculated_averages,
        'current_page': page_number,
        'understandability': understandability,
        'visited_pages': request.session['visited_pages'],
    }

    return render(request, 'problem4.html', context)


def problem5(request, page_number):
    
    visited_pages = request.session.get('visited_pages', [])
    
    if page_number not in visited_pages:
        visited_pages.append(page_number)
        request.session['visited_pages'] = visited_pages
    
    if request.method == 'POST':
        form = RatingForm5(request.POST)
        if form.is_valid():
            request.session['rating5_data'] = form.cleaned_data
            request.session['understandability51'] = form.cleaned_data.get('understandability51', 0)
            request.session['understandability52'] = form.cleaned_data.get('understandability52', 0)
            return redirect('problem6', page_number=page_number + 1)
    else:
        initial_data = {
            'error_description_51': request.session.get('rating5_data', {}).get('error_description_51', ''),
            'understandability51': request.session.get('rating5_data', {}).get('understandability51', ''),
            'error_description_52': request.session.get('rating5_data', {}).get('error_description_52', ''),
            'understandability52': request.session.get('rating5_data', {}).get('understandability52', ''),
        }
        form = RatingForm5(initial=initial_data)
    understandability = {f'understandability5{i}': request.session.get(f'understandability5{i}', 0) for i in range(1, 3)}

    tasubmissions = TASubmission.objects.all()

    average_ratings = {
        'feedback51_rating': [],
        'feedback52_rating': [],
        'feedback53_rating': [],
        'feedback54_rating': [],
        'feedback55_rating': [],
        'feedback56_rating': [],
        'feedback57_rating': [],
    }

    for submission in tasubmissions:
        average_ratings['feedback51_rating'].append(submission.feedback51_rating)
        average_ratings['feedback52_rating'].append(submission.feedback52_rating)
        average_ratings['feedback53_rating'].append(submission.feedback53_rating)
        average_ratings['feedback54_rating'].append(submission.feedback54_rating)
        average_ratings['feedback55_rating'].append(submission.feedback55_rating)
        average_ratings['feedback56_rating'].append(submission.feedback56_rating)
        average_ratings['feedback57_rating'].append(submission.feedback57_rating)

    calculated_averages = {key: (sum(values) / len(values) if values else 0) for key, values in average_ratings.items()}

    highest_feedback_key = max(calculated_averages, key=calculated_averages.get)

    feedback_content_map = {
        'feedback51_rating': ('content1', 'Feedback 51'),
        'feedback52_rating': ('content2', 'Feedback 52'),
        'feedback53_rating': ('content3', 'Feedback 53'),
        'feedback54_rating': ('content4', 'Feedback 54'),
        'feedback55_rating': ('content5', 'Feedback 55'),
        'feedback56_rating': ('content6', 'Feedback 56'),
        'feedback57_rating': ('content7', 'Feedback 57'),
    }

    highest_content_field, highest_feedback_name = feedback_content_map[highest_feedback_key]

    # Retrieve the latest two TAFeedback entries
    latest_feedbacks = TAFeedback.objects.order_by('-id')[:2]
    ta_feedback_1 = latest_feedbacks[0] if len(latest_feedbacks) > 0 else None
    ta_feedback_2 = latest_feedbacks[1] if len(latest_feedbacks) > 1 else None

    if highest_feedback_key == 'feedback56_rating':
        highest_rating_content = ta_feedback_1.ta_feedback5 if ta_feedback_1 else "No TA feedback available"
    elif highest_feedback_key == 'feedback57_rating':
        highest_rating_content = ta_feedback_2.ta_feedback5 if ta_feedback_2 else "No TA feedback available"
    else:
        highest_rated_feedback = Feedback.objects.filter(problem_id=5).first()

        if highest_rated_feedback:
            highest_rating_content = getattr(highest_rated_feedback, highest_content_field)  
        else:
            highest_rating_content = "No feedback available"

    context = {
        'form': form,
        'highest_rating_content': highest_rating_content,
        'highest_feedback_name': highest_feedback_name,
        'average_ratings': calculated_averages,
        'current_page': page_number,
        'understandability': understandability,
        'visited_pages': request.session['visited_pages'],
    }
    
    return render(request, 'problem5.html', context)


def problem6(request, page_number):
    
    visited_pages = request.session.get('visited_pages', [])
    
    if page_number not in visited_pages:
        visited_pages.append(page_number)
        request.session['visited_pages'] = visited_pages
    
    if request.method == 'POST':
        form = RatingForm6(request.POST)
        if form.is_valid():
            request.session['rating6_data'] = form.cleaned_data
            request.session['understandability61'] = form.cleaned_data.get('understandability61', 0)
            request.session['understandability62'] = form.cleaned_data.get('understandability62', 0)
            return redirect('problem7', page_number=page_number + 1)
    else:
        initial_data = {
            'error_description_61': request.session.get('rating6_data', {}).get('error_description_61', ''),
            'understandability61': request.session.get('rating6_data', {}).get('understandability61', ''),
            'error_description_62': request.session.get('rating6_data', {}).get('error_description_62', ''),
            'understandability62': request.session.get('rating6_data', {}).get('understandability62', ''),
        }
        form = RatingForm6(initial=initial_data)
    understandability = {f'understandability6{i}': request.session.get(f'understandability6{i}', 0) for i in range(1, 3)}

    tasubmissions = TASubmission.objects.all()

    average_ratings = {
        'feedback61_rating': [],
        'feedback62_rating': [],
        'feedback63_rating': [],
        'feedback64_rating': [],
        'feedback65_rating': [],
        'feedback66_rating': [],
        'feedback67_rating': [],
    }

    for submission in tasubmissions:
        average_ratings['feedback61_rating'].append(submission.feedback61_rating)
        average_ratings['feedback62_rating'].append(submission.feedback62_rating)
        average_ratings['feedback63_rating'].append(submission.feedback63_rating)
        average_ratings['feedback64_rating'].append(submission.feedback64_rating)
        average_ratings['feedback65_rating'].append(submission.feedback65_rating)
        average_ratings['feedback66_rating'].append(submission.feedback66_rating)
        average_ratings['feedback67_rating'].append(submission.feedback67_rating)

    calculated_averages = {key: (sum(values) / len(values) if values else 0) for key, values in average_ratings.items()}

    highest_feedback_key = max(calculated_averages, key=calculated_averages.get)

    feedback_content_map = {
        'feedback61_rating': ('content1', 'Feedback 61'),
        'feedback62_rating': ('content2', 'Feedback 62'),
        'feedback63_rating': ('content3', 'Feedback 63'),
        'feedback64_rating': ('content4', 'Feedback 64'),
        'feedback65_rating': ('content5', 'Feedback 65'),
        'feedback66_rating': ('content6', 'Feedback 66'),
        'feedback67_rating': ('content7', 'Feedback 67'),
    }

    highest_content_field, highest_feedback_name = feedback_content_map[highest_feedback_key]

    # Retrieve the latest two TAFeedback entries
    latest_feedbacks = TAFeedback.objects.order_by('-id')[:2]
    ta_feedback_1 = latest_feedbacks[0] if len(latest_feedbacks) > 0 else None
    ta_feedback_2 = latest_feedbacks[1] if len(latest_feedbacks) > 1 else None

    if highest_feedback_key == 'feedback66_rating':
        highest_rating_content = ta_feedback_1.ta_feedback6 if ta_feedback_1 else "No TA feedback available"
    elif highest_feedback_key == 'feedback67_rating':
        highest_rating_content = ta_feedback_2.ta_feedback6 if ta_feedback_2 else "No TA feedback available"
    else:
        highest_rated_feedback = Feedback.objects.filter(problem_id=6).first()

        if highest_rated_feedback:
            highest_rating_content = getattr(highest_rated_feedback, highest_content_field)  
        else:
            highest_rating_content = "No feedback available"

    context = {
        'form': form,
        'highest_rating_content': highest_rating_content,
        'highest_feedback_name': highest_feedback_name,
        'average_ratings': calculated_averages,
        'current_page': page_number,
        'understandability': understandability,
        'visited_pages': request.session['visited_pages'],
    }
    
    return render(request, 'problem6.html', context)


def problem7(request, page_number):
    
    visited_pages = request.session.get('visited_pages', [])
    
    if page_number not in visited_pages:
        visited_pages.append(page_number)
        request.session['visited_pages'] = visited_pages
    
    if request.method == 'POST':
        form = RatingForm7(request.POST)
        if form.is_valid():
            
            # Retrieve all session data
            participation_data = request.session.get('participation_data', {})
            rating1_data = request.session.get('rating1_data', {})
            rating2_data = request.session.get('rating2_data', {})
            rating3_data = request.session.get('rating3_data', {})
            rating4_data = request.session.get('rating4_data', {})
            rating5_data = request.session.get('rating5_data', {})
            rating6_data = request.session.get('rating6_data', {})
            rating7_data = form.cleaned_data
            request.session['understandability71'] = form.cleaned_data.get('understandability71', 0)
            request.session['understandability72'] = form.cleaned_data.get('understandability72', 0)

            # Combine all data
            complete_data = {
                **participation_data, **rating1_data, **rating2_data,
                **rating3_data, **rating4_data, **rating5_data, **rating6_data,
                **rating7_data
            }

            # Save to the database
            UserSubmission.objects.create(**complete_data)
            
            session_keys = [
                'participation_data', 'rating1_data', 'rating2_data',
                'rating3_data', 'rating4_data', 'rating5_data', 'rating6_data', 'understandability11', 'understandability12',
                'understandability21', 'understandability22', 'understandability31', 'understandability32', 'understandability41',
                'understandability42', 'understandability51', 'understandability52', 'understandability61', 'understandability62',
                'understandability71', 'understandability72'
            ]
            for key in session_keys:
                request.session.pop(key, None)

            reset_visited_pages(request)
            return redirect('success')
    else:
        initial_data = {
            'error_description_71': request.session.get('rating7_data', {}).get('error_description_71', ''),
            'understandability71': request.session.get('rating7_data', {}).get('understandability71', ''),
            'error_description_72': request.session.get('rating7_data', {}).get('error_description_72', ''),
            'understandability72': request.session.get('rating7_data', {}).get('understandability72', ''),
        }
        form = RatingForm7(initial=initial_data)
    understandability = {f'understandability7{i}': request.session.get(f'understandability7{i}', 0) for i in range(1, 3)}

    tasubmissions = TASubmission.objects.all()

    average_ratings = {
        'feedback71_rating': [],
        'feedback72_rating': [],
        'feedback73_rating': [],
        'feedback74_rating': [],
        'feedback75_rating': [],
        'feedback76_rating': [],
        'feedback77_rating': [],
    }

    for submission in tasubmissions:
        average_ratings['feedback71_rating'].append(submission.feedback71_rating)
        average_ratings['feedback72_rating'].append(submission.feedback72_rating)
        average_ratings['feedback73_rating'].append(submission.feedback73_rating)
        average_ratings['feedback74_rating'].append(submission.feedback74_rating)
        average_ratings['feedback75_rating'].append(submission.feedback75_rating)
        average_ratings['feedback76_rating'].append(submission.feedback76_rating)
        average_ratings['feedback77_rating'].append(submission.feedback77_rating)

    calculated_averages = {key: (sum(values) / len(values) if values else 0) for key, values in average_ratings.items()}

    highest_feedback_key = max(calculated_averages, key=calculated_averages.get)

    feedback_content_map = {
        'feedback71_rating': ('content1', 'Feedback 71'),
        'feedback72_rating': ('content2', 'Feedback 72'),
        'feedback73_rating': ('content3', 'Feedback 73'),
        'feedback74_rating': ('content4', 'Feedback 74'),
        'feedback75_rating': ('content5', 'Feedback 75'),
        'feedback76_rating': ('content6', 'Feedback 76'),
        'feedback77_rating': ('content7', 'Feedback 77'),
    }

    highest_content_field, highest_feedback_name = feedback_content_map[highest_feedback_key]

    # Retrieve the latest two TAFeedback entries
    latest_feedbacks = TAFeedback.objects.order_by('-id')[:2]
    ta_feedback_1 = latest_feedbacks[0] if len(latest_feedbacks) > 0 else None
    ta_feedback_2 = latest_feedbacks[1] if len(latest_feedbacks) > 1 else None

    if highest_feedback_key == 'feedback76_rating':
        highest_rating_content = ta_feedback_1.ta_feedback7 if ta_feedback_1 else "No TA feedback available"
    elif highest_feedback_key == 'feedback77_rating':
        highest_rating_content = ta_feedback_2.ta_feedback7 if ta_feedback_2 else "No TA feedback available"
    else:
        highest_rated_feedback = Feedback.objects.filter(problem_id=7).first()

        if highest_rated_feedback:
            highest_rating_content = getattr(highest_rated_feedback, highest_content_field)  
        else:
            highest_rating_content = "No feedback available"

    context = {
        'form': form,
        'highest_rating_content': highest_rating_content,
        'highest_feedback_name': highest_feedback_name,
        'average_ratings': calculated_averages,
        'current_page': page_number,
        'understandability': understandability,
        'visited_pages': request.session['visited_pages'],
    }

    return render(request, 'problem7.html', context)


def success(request):
    return render(request, 'success.html')

def ta_overview(request):
    return render(request, 'ta_overview.html')

def taproblem1(request, page_number):
    
    visited_pages = request.session.get('visited_pages', [])
    
    if page_number not in visited_pages:
        visited_pages.append(page_number)
        request.session['visited_pages'] = visited_pages
        
    feedback1 = "No feedback yet!"
    feedback2 = "No feedback yet!"
    
    feedbacks = TAFeedback.objects.order_by('-id')[:2]

    if len(feedbacks) > 0:
        feedback1 = feedbacks[0].ta_feedback1
    if len(feedbacks) > 1:
        feedback2 = feedbacks[1].ta_feedback1
        
    if request.method == 'POST':
        # Instantiate the form with POST data
        form = TARatingForm1(request.POST)
        
        if form.is_valid():
            # Extract form data
            feedback1_rating = form.cleaned_data['feedback11_rating']
            feedback2_rating = form.cleaned_data['feedback12_rating']
            feedback3_rating = form.cleaned_data['feedback13_rating']
            feedback4_rating = form.cleaned_data['feedback14_rating']
            feedback5_rating = form.cleaned_data['feedback15_rating']
            feedback6_rating = form.cleaned_data['feedback16_rating']
            feedback7_rating = form.cleaned_data['feedback17_rating']
            
            # Store the feedback in the session
            request.session['feedback11_rating'] = feedback1_rating
            request.session['feedback12_rating'] = feedback2_rating
            request.session['feedback13_rating'] = feedback3_rating
            request.session['feedback14_rating'] = feedback4_rating
            request.session['feedback15_rating'] = feedback5_rating
            request.session['feedback16_rating'] = feedback6_rating
            request.session['feedback17_rating'] = feedback7_rating
            
            
            request.session['feedback11_rating'] = form.cleaned_data.get('feedback11_rating', 0)
            request.session['feedback12_rating'] = form.cleaned_data.get('feedback12_rating', 0)
            request.session['feedback13_rating'] = form.cleaned_data.get('feedback13_rating', 0)
            request.session['feedback14_rating'] = form.cleaned_data.get('feedback14_rating', 0)
            request.session['feedback15_rating'] = form.cleaned_data.get('feedback15_rating', 0)
            request.session['feedback16_rating'] = form.cleaned_data.get('feedback16_rating', 0)
            request.session['feedback17_rating'] = form.cleaned_data.get('feedback17_rating', 0)
            
            # Redirect to the next problem page
            return redirect('taproblem2', page_number=page_number + 1)  # Replace with the actual URL for the next problem

    else:
        # GET request, pre-populate form with session data if available
        initial_data = {
            'feedback11_rating': request.session.get('feedback11_rating', ''),
            'feedback12_rating': request.session.get('feedback12_rating', ''),
            'feedback13_rating': request.session.get('feedback13_rating', ''),
            'feedback14_rating': request.session.get('feedback14_rating', ''),
            'feedback15_rating': request.session.get('feedback15_rating', ''),
            'feedback16_rating': request.session.get('feedback16_rating', ''),
            'feedback17_rating': request.session.get('feedback17_rating', ''),
        }
        
        form = TARatingForm1(initial=initial_data)
        
    feedback_data = {f'feedback1{i}': request.session.get(f'feedback1{i}_rating', 0) for i in range(1, 8)}
    return render(request, 'taproblem1.html', {
        'form': form,
        'ta1_feedback1': feedback1,
        'ta2_feedback1': feedback2,
        'current_page': page_number,
        'feedback_data': feedback_data,
        'visited_pages': request.session['visited_pages'],
        })

def taproblem2(request, page_number):
    
    visited_pages = request.session.get('visited_pages', [])
    
    if page_number not in visited_pages:
        visited_pages.append(page_number)
        request.session['visited_pages'] = visited_pages
        
    feedback1 = "No feedback yet!"
    feedback2 = "No feedback yet!"
    
    feedbacks = TAFeedback.objects.order_by('-id')[:2]

    if len(feedbacks) > 0:
        feedback1 = feedbacks[0].ta_feedback2
    if len(feedbacks) > 1:
        feedback2 = feedbacks[1].ta_feedback2
        
    if request.method == 'POST':
        
        form = TARatingForm2(request.POST)
        
        if form.is_valid():
            
            feedback1_rating = form.cleaned_data['feedback21_rating']
            feedback2_rating = form.cleaned_data['feedback22_rating']
            feedback3_rating = form.cleaned_data['feedback23_rating']
            feedback4_rating = form.cleaned_data['feedback24_rating']
            feedback5_rating = form.cleaned_data['feedback25_rating']
            feedback6_rating = form.cleaned_data['feedback26_rating']
            feedback7_rating = form.cleaned_data['feedback27_rating']
            
            
            request.session['feedback21_rating'] = feedback1_rating
            request.session['feedback22_rating'] = feedback2_rating
            request.session['feedback23_rating'] = feedback3_rating
            request.session['feedback24_rating'] = feedback4_rating
            request.session['feedback25_rating'] = feedback5_rating
            request.session['feedback26_rating'] = feedback6_rating
            request.session['feedback27_rating'] = feedback7_rating
            
            request.session['feedback21_rating'] = form.cleaned_data.get('feedback21_rating', 0)
            request.session['feedback22_rating'] = form.cleaned_data.get('feedback22_rating', 0)
            request.session['feedback23_rating'] = form.cleaned_data.get('feedback23_rating', 0)
            request.session['feedback24_rating'] = form.cleaned_data.get('feedback24_rating', 0)
            request.session['feedback25_rating'] = form.cleaned_data.get('feedback25_rating', 0)
            request.session['feedback26_rating'] = form.cleaned_data.get('feedback26_rating', 0)
            request.session['feedback27_rating'] = form.cleaned_data.get('feedback27_rating', 0)
            
            return redirect('taproblem3', page_number=page_number + 1) 

    else:
        
        initial_data = {
            'feedback21_rating': request.session.get('feedback21_rating', ''),
            'feedback22_rating': request.session.get('feedback22_rating', ''),
            'feedback23_rating': request.session.get('feedback23_rating', ''),
            'feedback24_rating': request.session.get('feedback24_rating', ''),
            'feedback25_rating': request.session.get('feedback25_rating', ''),
            'feedback26_rating': request.session.get('feedback26_rating', ''),
            'feedback27_rating': request.session.get('feedback27_rating', ''),
        }
        
        form = TARatingForm2(initial=initial_data)
        
    feedback_data = {f'feedback2{i}': request.session.get(f'feedback2{i}_rating', 0) for i in range(1, 8)}

    return render(request, 'taproblem2.html', {
        'form': form,
        'ta1_feedback2': feedback1,
        'ta2_feedback2': feedback2,
        'current_page': page_number,
        'feedback_data': feedback_data,
        'visited_pages': request.session['visited_pages'],
        })

def taproblem3(request, page_number):
    
    visited_pages = request.session.get('visited_pages', [])
    
    if page_number not in visited_pages:
        visited_pages.append(page_number)
        request.session['visited_pages'] = visited_pages
        
    feedback1 = "No feedback yet!"
    feedback2 = "No feedback yet!"
    
    feedbacks = TAFeedback.objects.order_by('-id')[:2]

    if len(feedbacks) > 0:
        feedback1 = feedbacks[0].ta_feedback3
    if len(feedbacks) > 1:
        feedback2 = feedbacks[1].ta_feedback3
        
    if request.method == 'POST':
        
        form = TARatingForm3(request.POST)
        
        if form.is_valid():
            
            feedback1_rating = form.cleaned_data['feedback31_rating']
            feedback2_rating = form.cleaned_data['feedback32_rating']
            feedback3_rating = form.cleaned_data['feedback33_rating']
            feedback4_rating = form.cleaned_data['feedback34_rating']
            feedback5_rating = form.cleaned_data['feedback35_rating']
            feedback6_rating = form.cleaned_data['feedback36_rating']
            feedback7_rating = form.cleaned_data['feedback37_rating']
            
            request.session['feedback31_rating'] = feedback1_rating
            request.session['feedback32_rating'] = feedback2_rating
            request.session['feedback33_rating'] = feedback3_rating
            request.session['feedback34_rating'] = feedback4_rating
            request.session['feedback35_rating'] = feedback5_rating
            request.session['feedback36_rating'] = feedback6_rating
            request.session['feedback37_rating'] = feedback7_rating
            
            request.session['feedback31_rating'] = form.cleaned_data.get('feedback31_rating', 0)
            request.session['feedback32_rating'] = form.cleaned_data.get('feedback32_rating', 0)
            request.session['feedback33_rating'] = form.cleaned_data.get('feedback33_rating', 0)
            request.session['feedback34_rating'] = form.cleaned_data.get('feedback34_rating', 0)
            request.session['feedback35_rating'] = form.cleaned_data.get('feedback35_rating', 0)
            request.session['feedback36_rating'] = form.cleaned_data.get('feedback36_rating', 0)
            request.session['feedback37_rating'] = form.cleaned_data.get('feedback37_rating', 0)
            
            return redirect('taproblem4', page_number=page_number + 1)

    else:
        
        initial_data = {
            'feedback31_rating': request.session.get('feedback31_rating', ''),
            'feedback32_rating': request.session.get('feedback32_rating', ''),
            'feedback33_rating': request.session.get('feedback33_rating', ''),
            'feedback34_rating': request.session.get('feedback34_rating', ''),
            'feedback35_rating': request.session.get('feedback35_rating', ''),
            'feedback36_rating': request.session.get('feedback36_rating', ''),
            'feedback37_rating': request.session.get('feedback37_rating', ''),
        }
        
        form = TARatingForm3(initial=initial_data)
        
    feedback_data = {f'feedback3{i}': request.session.get(f'feedback3{i}_rating', 0) for i in range(1, 8)}

    return render(request, 'taproblem3.html', {
        'form': form,
        'ta1_feedback3': feedback1,
        'ta2_feedback3': feedback2,
        'feedback_data': feedback_data,
        'current_page': page_number,
        'visited_pages': request.session['visited_pages'],
        })


def taproblem4(request, page_number):
    
    visited_pages = request.session.get('visited_pages', [])
    
    if page_number not in visited_pages:
        visited_pages.append(page_number)
        request.session['visited_pages'] = visited_pages
        
    feedback1 = "No feedback yet!"
    feedback2 = "No feedback yet!"
    
    feedbacks = TAFeedback.objects.order_by('-id')[:2]

    if len(feedbacks) > 0:
        feedback1 = feedbacks[0].ta_feedback4
    if len(feedbacks) > 1:
        feedback2 = feedbacks[1].ta_feedback4
        
    if request.method == 'POST':
        
        form = TARatingForm4(request.POST)
        
        if form.is_valid():
            
            feedback1_rating = form.cleaned_data['feedback41_rating']
            feedback2_rating = form.cleaned_data['feedback42_rating']
            feedback3_rating = form.cleaned_data['feedback43_rating']
            feedback4_rating = form.cleaned_data['feedback44_rating']
            feedback5_rating = form.cleaned_data['feedback45_rating']
            feedback6_rating = form.cleaned_data['feedback46_rating']
            feedback7_rating = form.cleaned_data['feedback47_rating']
            
            request.session['feedback41_rating'] = feedback1_rating
            request.session['feedback42_rating'] = feedback2_rating
            request.session['feedback43_rating'] = feedback3_rating
            request.session['feedback44_rating'] = feedback4_rating
            request.session['feedback45_rating'] = feedback5_rating
            request.session['feedback46_rating'] = feedback6_rating
            request.session['feedback47_rating'] = feedback7_rating
            
            request.session['feedback41_rating'] = form.cleaned_data.get('feedback41_rating', 0)
            request.session['feedback42_rating'] = form.cleaned_data.get('feedback42_rating', 0)
            request.session['feedback43_rating'] = form.cleaned_data.get('feedback43_rating', 0)
            request.session['feedback44_rating'] = form.cleaned_data.get('feedback44_rating', 0)
            request.session['feedback45_rating'] = form.cleaned_data.get('feedback45_rating', 0)
            request.session['feedback46_rating'] = form.cleaned_data.get('feedback46_rating', 0)
            request.session['feedback47_rating'] = form.cleaned_data.get('feedback47_rating', 0)
            
            return redirect('taproblem5', page_number=page_number + 1)  

    else:
        
        initial_data = {
            'feedback41_rating': request.session.get('feedback41_rating', ''),
            'feedback42_rating': request.session.get('feedback42_rating', ''),
            'feedback43_rating': request.session.get('feedback43_rating', ''),
            'feedback44_rating': request.session.get('feedback44_rating', ''),
            'feedback45_rating': request.session.get('feedback45_rating', ''),
            'feedback46_rating': request.session.get('feedback46_rating', ''),
            'feedback47_rating': request.session.get('feedback47_rating', ''),
        }
        
        form = TARatingForm4(initial=initial_data)
        
    feedback_data = {f'feedback4{i}': request.session.get(f'feedback4{i}_rating', 0) for i in range(1, 8)}

    return render(request, 'taproblem4.html', {
        'form': form,
        'ta1_feedback4': feedback1,
        'ta2_feedback4': feedback2,
        'feedback_data': feedback_data,
        'current_page': page_number,
        'visited_pages': request.session['visited_pages'],
        })


def taproblem5(request, page_number):
    
    visited_pages = request.session.get('visited_pages', [])
    
    if page_number not in visited_pages:
        visited_pages.append(page_number)
        request.session['visited_pages'] = visited_pages
        
    feedback1 = "No feedback yet!"
    feedback2 = "No feedback yet!"
    
    feedbacks = TAFeedback.objects.order_by('-id')[:2]

    if len(feedbacks) > 0:
        feedback1 = feedbacks[0].ta_feedback5
    if len(feedbacks) > 1:
        feedback2 = feedbacks[1].ta_feedback5
        
    if request.method == 'POST':
        
        form = TARatingForm5(request.POST)
        
        if form.is_valid():
            
            feedback1_rating = form.cleaned_data['feedback51_rating']
            feedback2_rating = form.cleaned_data['feedback52_rating']
            feedback3_rating = form.cleaned_data['feedback53_rating']
            feedback4_rating = form.cleaned_data['feedback54_rating']
            feedback5_rating = form.cleaned_data['feedback55_rating']
            feedback6_rating = form.cleaned_data['feedback56_rating']
            feedback7_rating = form.cleaned_data['feedback57_rating']
            
            request.session['feedback51_rating'] = feedback1_rating
            request.session['feedback52_rating'] = feedback2_rating
            request.session['feedback53_rating'] = feedback3_rating
            request.session['feedback54_rating'] = feedback4_rating
            request.session['feedback55_rating'] = feedback5_rating
            request.session['feedback56_rating'] = feedback6_rating
            request.session['feedback57_rating'] = feedback7_rating
            
            request.session['feedback51_rating'] = form.cleaned_data.get('feedback51_rating', 0)
            request.session['feedback52_rating'] = form.cleaned_data.get('feedback52_rating', 0)
            request.session['feedback53_rating'] = form.cleaned_data.get('feedback53_rating', 0)
            request.session['feedback54_rating'] = form.cleaned_data.get('feedback54_rating', 0)
            request.session['feedback55_rating'] = form.cleaned_data.get('feedback55_rating', 0)
            request.session['feedback56_rating'] = form.cleaned_data.get('feedback56_rating', 0)
            request.session['feedback57_rating'] = form.cleaned_data.get('feedback57_rating', 0)
            
            return redirect('taproblem6', page_number=page_number + 1)

    else:
        
        initial_data = {
            'feedback51_rating': request.session.get('feedback51_rating', ''),
            'feedback52_rating': request.session.get('feedback52_rating', ''),
            'feedback53_rating': request.session.get('feedback53_rating', ''),
            'feedback54_rating': request.session.get('feedback54_rating', ''),
            'feedback55_rating': request.session.get('feedback55_rating', ''),
            'feedback56_rating': request.session.get('feedback56_rating', ''),
            'feedback57_rating': request.session.get('feedback57_rating', ''),
        }
        
        form = TARatingForm5(initial=initial_data)
        
    feedback_data = {f'feedback5{i}': request.session.get(f'feedback5{i}_rating', 0) for i in range(1, 8)}

    return render(request, 'taproblem5.html', {
        'form': form,
        'ta1_feedback5': feedback1,
        'ta2_feedback5': feedback2,
        'feedback_data': feedback_data,
        'current_page': page_number,
        'visited_pages': request.session['visited_pages'],
        })



def taproblem6(request, page_number):
    
    visited_pages = request.session.get('visited_pages', [])
    
    if page_number not in visited_pages:
        visited_pages.append(page_number)
        request.session['visited_pages'] = visited_pages
        
    feedback1 = "No feedback yet!"
    feedback2 = "No feedback yet!"
    
    feedbacks = TAFeedback.objects.order_by('-id')[:2]

    if len(feedbacks) > 0:
        feedback1 = feedbacks[0].ta_feedback6
    if len(feedbacks) > 1:
        feedback2 = feedbacks[1].ta_feedback6
        
    if request.method == 'POST':
        
        form = TARatingForm6(request.POST)
        
        if form.is_valid():
            
            feedback1_rating = form.cleaned_data['feedback61_rating']
            feedback2_rating = form.cleaned_data['feedback62_rating']
            feedback3_rating = form.cleaned_data['feedback63_rating']
            feedback4_rating = form.cleaned_data['feedback64_rating']
            feedback5_rating = form.cleaned_data['feedback65_rating']
            feedback6_rating = form.cleaned_data['feedback66_rating']
            feedback7_rating = form.cleaned_data['feedback67_rating']
            
            request.session['feedback61_rating'] = feedback1_rating
            request.session['feedback62_rating'] = feedback2_rating
            request.session['feedback63_rating'] = feedback3_rating
            request.session['feedback64_rating'] = feedback4_rating
            request.session['feedback65_rating'] = feedback5_rating
            request.session['feedback66_rating'] = feedback6_rating
            request.session['feedback67_rating'] = feedback7_rating
            
            request.session['feedback61_rating'] = form.cleaned_data.get('feedback61_rating', 0)
            request.session['feedback62_rating'] = form.cleaned_data.get('feedback62_rating', 0)
            request.session['feedback63_rating'] = form.cleaned_data.get('feedback63_rating', 0)
            request.session['feedback64_rating'] = form.cleaned_data.get('feedback64_rating', 0)
            request.session['feedback65_rating'] = form.cleaned_data.get('feedback65_rating', 0)
            request.session['feedback66_rating'] = form.cleaned_data.get('feedback66_rating', 0)
            request.session['feedback67_rating'] = form.cleaned_data.get('feedback67_rating', 0)
            
            return redirect('taproblem7', page_number=page_number + 1) 

    else:
        
        initial_data = {
            'feedback61_rating': request.session.get('feedback61_rating', ''),
            'feedback62_rating': request.session.get('feedback62_rating', ''),
            'feedback63_rating': request.session.get('feedback63_rating', ''),
            'feedback64_rating': request.session.get('feedback64_rating', ''),
            'feedback65_rating': request.session.get('feedback65_rating', ''),
            'feedback66_rating': request.session.get('feedback66_rating', ''),
            'feedback67_rating': request.session.get('feedback67_rating', ''),
        }
        form = TARatingForm6(initial=initial_data)
    feedback_data = {f'feedback6{i}': request.session.get(f'feedback6{i}_rating', 0) for i in range(1, 8)}

    return render(request, 'taproblem6.html', {
        'form': form,
        'ta1_feedback6': feedback1,
        'ta2_feedback6': feedback2,
        'feedback_data': feedback_data,
        'current_page': page_number,
        'visited_pages': request.session['visited_pages'],
        })

def taproblem7(request, page_number):
    
    visited_pages = request.session.get('visited_pages', [])
    
    if page_number not in visited_pages:
        visited_pages.append(page_number)
        request.session['visited_pages'] = visited_pages
        
    feedback1 = "No feedback yet!"
    feedback2 = "No feedback yet!"
    
    feedbacks = TAFeedback.objects.order_by('-id')[:2]

    if len(feedbacks) > 0:
        feedback1 = feedbacks[0].ta_feedback7
    if len(feedbacks) > 1:
        feedback2 = feedbacks[1].ta_feedback7
        
    if request.method == 'POST':
        
        form = TARatingForm7(request.POST)
        
        if form.is_valid():
            
            feedback1_rating = form.cleaned_data['feedback71_rating']
            feedback2_rating = form.cleaned_data['feedback72_rating']
            feedback3_rating = form.cleaned_data['feedback73_rating']
            feedback4_rating = form.cleaned_data['feedback74_rating']
            feedback5_rating = form.cleaned_data['feedback75_rating']
            feedback6_rating = form.cleaned_data['feedback76_rating']
            feedback7_rating = form.cleaned_data['feedback77_rating']

            request.session['feedback71_rating'] = feedback1_rating
            request.session['feedback72_rating'] = feedback2_rating
            request.session['feedback73_rating'] = feedback3_rating
            request.session['feedback74_rating'] = feedback4_rating
            request.session['feedback75_rating'] = feedback5_rating
            request.session['feedback76_rating'] = feedback6_rating
            request.session['feedback77_rating'] = feedback7_rating
            
            request.session['feedback71_rating'] = form.cleaned_data.get('feedback71_rating', 0)
            request.session['feedback72_rating'] = form.cleaned_data.get('feedback72_rating', 0)
            request.session['feedback73_rating'] = form.cleaned_data.get('feedback73_rating', 0)
            request.session['feedback74_rating'] = form.cleaned_data.get('feedback74_rating', 0)
            request.session['feedback75_rating'] = form.cleaned_data.get('feedback75_rating', 0)
            request.session['feedback76_rating'] = form.cleaned_data.get('feedback76_rating', 0)
            request.session['feedback77_rating'] = form.cleaned_data.get('feedback77_rating', 0)
            
            participation_data = request.session.get('participation_data', {})

            name = participation_data.get('name', 'Unknown')
            email = participation_data.get('email', 'Unknown')
            organisation = participation_data.get('organisation', 'Unknown')
            rollno = participation_data.get('rollno', 'Unknown')

            feedback_data = {
                'name': name,
                'email': email,
                'organisation': organisation,
                'rollno': rollno,
                'feedback11_rating': request.session.get('feedback11_rating'),
                'feedback12_rating': request.session.get('feedback12_rating'),
                'feedback13_rating': request.session.get('feedback13_rating'),
                'feedback14_rating': request.session.get('feedback14_rating'),
                'feedback15_rating': request.session.get('feedback15_rating'),
                'feedback16_rating': request.session.get('feedback16_rating'),
                'feedback17_rating': request.session.get('feedback17_rating'),

                'feedback21_rating': request.session.get('feedback21_rating'),
                'feedback22_rating': request.session.get('feedback22_rating'),
                'feedback23_rating': request.session.get('feedback23_rating'),
                'feedback24_rating': request.session.get('feedback24_rating'),
                'feedback25_rating': request.session.get('feedback25_rating'),
                'feedback26_rating': request.session.get('feedback26_rating'),
                'feedback27_rating': request.session.get('feedback27_rating'),

                'feedback31_rating': request.session.get('feedback31_rating'),
                'feedback32_rating': request.session.get('feedback32_rating'),
                'feedback33_rating': request.session.get('feedback33_rating'),
                'feedback34_rating': request.session.get('feedback34_rating'),
                'feedback35_rating': request.session.get('feedback35_rating'),
                'feedback36_rating': request.session.get('feedback36_rating'),
                'feedback37_rating': request.session.get('feedback37_rating'),

                'feedback41_rating': request.session.get('feedback41_rating'),
                'feedback42_rating': request.session.get('feedback42_rating'),
                'feedback43_rating': request.session.get('feedback43_rating'),
                'feedback44_rating': request.session.get('feedback44_rating'),
                'feedback45_rating': request.session.get('feedback45_rating'),
                'feedback46_rating': request.session.get('feedback46_rating'),
                'feedback47_rating': request.session.get('feedback47_rating'),

                'feedback51_rating': request.session.get('feedback51_rating'),
                'feedback52_rating': request.session.get('feedback52_rating'),
                'feedback53_rating': request.session.get('feedback53_rating'),
                'feedback54_rating': request.session.get('feedback54_rating'),
                'feedback55_rating': request.session.get('feedback55_rating'),
                'feedback56_rating': request.session.get('feedback56_rating'),
                'feedback57_rating': request.session.get('feedback57_rating'),

                'feedback61_rating': request.session.get('feedback61_rating'),
                'feedback62_rating': request.session.get('feedback62_rating'),
                'feedback63_rating': request.session.get('feedback63_rating'),
                'feedback64_rating': request.session.get('feedback64_rating'),
                'feedback65_rating': request.session.get('feedback65_rating'),
                'feedback66_rating': request.session.get('feedback66_rating'),
                'feedback67_rating': request.session.get('feedback67_rating'),

                'feedback71_rating': feedback1_rating,
                'feedback72_rating': feedback2_rating,
                'feedback73_rating': feedback3_rating,
                'feedback74_rating': feedback4_rating,
                'feedback75_rating': feedback5_rating,
                'feedback76_rating': feedback6_rating,
                'feedback77_rating': feedback7_rating,
            }

            feedback = TASubmission(**feedback_data)
            feedback.save()

            request.session.pop('feedback11_rating', None)
            request.session.pop('feedback12_rating', None)
            request.session.pop('feedback13_rating', None)
            request.session.pop('feedback14_rating', None)
            request.session.pop('feedback15_rating', None)
            request.session.pop('feedback16_rating', None)
            request.session.pop('feedback17_rating', None)

            request.session.pop('feedback21_rating', None)
            request.session.pop('feedback22_rating', None)
            request.session.pop('feedback23_rating', None)
            request.session.pop('feedback24_rating', None)
            request.session.pop('feedback25_rating', None)
            request.session.pop('feedback26_rating', None)
            request.session.pop('feedback27_rating', None)

            request.session.pop('feedback31_rating', None)
            request.session.pop('feedback32_rating', None)
            request.session.pop('feedback33_rating', None)
            request.session.pop('feedback34_rating', None)
            request.session.pop('feedback35_rating', None)
            request.session.pop('feedback36_rating', None)
            request.session.pop('feedback37_rating', None)

            request.session.pop('feedback41_rating', None)
            request.session.pop('feedback42_rating', None)
            request.session.pop('feedback43_rating', None)
            request.session.pop('feedback44_rating', None)
            request.session.pop('feedback45_rating', None)
            request.session.pop('feedback46_rating', None)
            request.session.pop('feedback47_rating', None)

            request.session.pop('feedback51_rating', None)
            request.session.pop('feedback52_rating', None)
            request.session.pop('feedback53_rating', None)
            request.session.pop('feedback54_rating', None)
            request.session.pop('feedback55_rating', None)
            request.session.pop('feedback56_rating', None)
            request.session.pop('feedback57_rating', None)

            request.session.pop('feedback61_rating', None)
            request.session.pop('feedback62_rating', None)
            request.session.pop('feedback63_rating', None)
            request.session.pop('feedback64_rating', None)
            request.session.pop('feedback65_rating', None)
            request.session.pop('feedback66_rating', None)
            request.session.pop('feedback67_rating', None)

            request.session.pop('feedback71_rating', None)
            request.session.pop('feedback72_rating', None)
            request.session.pop('feedback73_rating', None)
            request.session.pop('feedback74_rating', None)
            request.session.pop('feedback75_rating', None)
            request.session.pop('feedback76_rating', None)
            request.session.pop('feedback77_rating', None)

            request.session.pop('participation_data', None)

            reset_visited_pages(request)
            
            return redirect('success') 

    else:
        
        initial_data = {
            'feedback71_rating': request.session.get('feedback71_rating', ''),
            'feedback72_rating': request.session.get('feedback72_rating', ''),
            'feedback73_rating': request.session.get('feedback73_rating', ''),
            'feedback74_rating': request.session.get('feedback74_rating', ''),
            'feedback75_rating': request.session.get('feedback75_rating', ''),
            'feedback76_rating': request.session.get('feedback76_rating', ''),
            'feedback77_rating': request.session.get('feedback77_rating', ''),
        }
        form = TARatingForm7(initial=initial_data)
    feedback_data = {f'feedback7{i}': request.session.get(f'feedback7{i}_rating', 0) for i in range(1, 8)}

    return render(request, 'taproblem7.html', {
        'form': form,
        'ta1_feedback7': feedback1,
        'ta2_feedback7': feedback2,
        'feedback_data': feedback_data,
        'current_page': page_number,
        'visited_pages': request.session['visited_pages'],
        })

def ta_overview2(request):
    return render(request, 'ta_overview2.html')

def tafeedback1(request, page_number):
    
    visited_pages = request.session.get('visited_pages', [])
    
    if page_number not in visited_pages:
        visited_pages.append(page_number)
        request.session['visited_pages'] = visited_pages
        
    # Handle POST request
    if request.method == 'POST':
        form = TAFeedbackForm1(request.POST)
        if form.is_valid():
            # Save the feedback data
            request.session['taproblem1_feedback'] = form.cleaned_data
            
            # Save the elapsed time if provided
            elapsed_time = request.POST.get('elapsed_time1')
            if elapsed_time:
                try:
                    request.session['taproblem1_elapsed_time'] = int(elapsed_time)
                except ValueError:
                    request.session['taproblem1_elapsed_time'] = 0
            
            # Redirect to the next page
            return redirect('tafeedback2', page_number=page_number + 1)
    
    else:
        # On GET request, retrieve initial data and saved elapsed time
        initial_data = request.session.get('taproblem1_feedback', {})
        saved_elapsed_time = request.session.get('taproblem1_elapsed_time', 0)  # Default to 0 if not set
        form = TAFeedbackForm1(initial=initial_data)

    # Pass form, current page, visited pages, and the saved elapsed time to the template
    return render(request, 'tafeedback1.html', {
        'form': form,
        'current_page': page_number,
        'visited_pages': request.session['visited_pages'],
        'saved_elapsed_time': saved_elapsed_time  # Pass saved elapsed time to the template
    })


def tafeedback2(request, page_number):
    
    visited_pages = request.session.get('visited_pages', [])
    
    if page_number not in visited_pages:
        visited_pages.append(page_number)
        request.session['visited_pages'] = visited_pages
        
    if request.method == 'POST':
        form = TAFeedbackForm2(request.POST)
        if form.is_valid():
            request.session['taproblem2_feedback'] = form.cleaned_data
            elapsed_time = request.POST.get('elapsed_time2')
            if elapsed_time:
                try:
                    request.session['taproblem2_elapsed_time'] = int(elapsed_time)
                except ValueError:
                    request.session['taproblem2_elapsed_time'] = 0

            return redirect('tafeedback3', page_number=page_number + 1)
    else:
        initial_data = request.session.get('taproblem2_feedback', {})
        saved_elapsed_time = request.session.get('taproblem2_elapsed_time', 0)
        form = TAFeedbackForm2(initial=initial_data)

    return render(request, 'tafeedback2.html', {
        'form': form,
        'current_page': page_number,
        'visited_pages': request.session['visited_pages'],
        'saved_elapsed_time': saved_elapsed_time
    })

def tafeedback3(request, page_number):
    
    visited_pages = request.session.get('visited_pages', [])
    
    if page_number not in visited_pages:
        visited_pages.append(page_number)
        request.session['visited_pages'] = visited_pages
        
    if request.method == 'POST':
        form = TAFeedbackForm3(request.POST)
        if form.is_valid():
            request.session['taproblem3_feedback'] = form.cleaned_data
            elapsed_time = request.POST.get('elapsed_time3')
            if elapsed_time:
                try:
                    request.session['taproblem3_elapsed_time'] = int(elapsed_time)
                except ValueError:
                    request.session['taproblem3_elapsed_time'] = 0

            return redirect('tafeedback4', page_number=page_number + 1)
    else:
        initial_data = request.session.get('taproblem3_feedback', {})
        saved_elapsed_time = request.session.get('taproblem3_elapsed_time', 0)
        form = TAFeedbackForm3(initial=initial_data)

    return render(request, 'tafeedback3.html', {
        'form': form,
        'current_page': page_number,
        'visited_pages': request.session['visited_pages'],
        'saved_elapsed_time': saved_elapsed_time
    })

def tafeedback4(request, page_number):
    
    visited_pages = request.session.get('visited_pages', [])
    
    if page_number not in visited_pages:
        visited_pages.append(page_number)
        request.session['visited_pages'] = visited_pages
        
    if request.method == 'POST':
        form = TAFeedbackForm4(request.POST)
        if form.is_valid():
            request.session['taproblem4_feedback'] = form.cleaned_data
            elapsed_time = request.POST.get('elapsed_time4')
            if elapsed_time:
                try:
                    request.session['taproblem4_elapsed_time'] = int(elapsed_time)
                except ValueError:
                    request.session['taproblem4_elapsed_time'] = 0

            return redirect('tafeedback5', page_number=page_number + 1)
    else:
        initial_data = request.session.get('taproblem4_feedback', {})
        saved_elapsed_time = request.session.get('taproblem4_elapsed_time', 0)
        form = TAFeedbackForm4(initial=initial_data)

    return render(request, 'tafeedback4.html', {
        'form': form,
        'current_page': page_number,
        'visited_pages': request.session['visited_pages'],
        'saved_elapsed_time': saved_elapsed_time
    })

def tafeedback5(request, page_number):
    
    visited_pages = request.session.get('visited_pages', [])
    
    if page_number not in visited_pages:
        visited_pages.append(page_number)
        request.session['visited_pages'] = visited_pages
        
    if request.method == 'POST':
        form = TAFeedbackForm5(request.POST)
        if form.is_valid():
            request.session['taproblem5_feedback'] = form.cleaned_data
            elapsed_time = request.POST.get('elapsed_time5')
            if elapsed_time:
                try:
                    request.session['taproblem5_elapsed_time'] = int(elapsed_time)
                except ValueError:
                    request.session['taproblem5_elapsed_time'] = 0

            return redirect('tafeedback6', page_number=page_number + 1)
    else:
        initial_data = request.session.get('taproblem5_feedback', {})
        saved_elapsed_time = request.session.get('taproblem5_elapsed_time', 0)
        form = TAFeedbackForm5(initial=initial_data)

    return render(request, 'tafeedback5.html', {
        'form': form,
        'current_page': page_number,
        'visited_pages': request.session['visited_pages'],
        'saved_elapsed_time': saved_elapsed_time
    })

def tafeedback6(request, page_number):
    
    visited_pages = request.session.get('visited_pages', [])
    
    if page_number not in visited_pages:
        visited_pages.append(page_number)
        request.session['visited_pages'] = visited_pages
        
    if request.method == 'POST':
        form = TAFeedbackForm6(request.POST)
        if form.is_valid():
            request.session['taproblem6_feedback'] = form.cleaned_data
            elapsed_time = request.POST.get('elapsed_time6')
            if elapsed_time:
                try:
                    request.session['taproblem6_elapsed_time'] = int(elapsed_time)
                except ValueError:
                    request.session['taproblem6_elapsed_time'] = 0

            return redirect('tafeedback7', page_number=page_number + 1)
    else:
        initial_data = request.session.get('taproblem6_feedback', {})
        saved_elapsed_time = request.session.get('taproblem6_elapsed_time', 0)
        form = TAFeedbackForm6(initial=initial_data)

    return render(request, 'tafeedback6.html', {
        'form': form,
        'current_page': page_number,
        'visited_pages': request.session['visited_pages'],
        'saved_elapsed_time': saved_elapsed_time
    })

def tafeedback7(request, page_number):
    
    visited_pages = request.session.get('visited_pages', [])
    
    if page_number not in visited_pages:
        visited_pages.append(page_number)
        request.session['visited_pages'] = visited_pages
        
    if request.method == 'POST':
        form = TAFeedbackForm7(request.POST)
        if form.is_valid():
            
            participation_data = request.session.get('participation_data', {})
            feedback1_data = request.session.get('taproblem1_feedback', {})
            feedback2_data = request.session.get('taproblem2_feedback', {})
            feedback3_data = request.session.get('taproblem3_feedback', {})
            feedback4_data = request.session.get('taproblem4_feedback', {})
            feedback5_data = request.session.get('taproblem5_feedback', {})
            feedback6_data = request.session.get('taproblem6_feedback', {})
            feedback7_data = form.cleaned_data

            missing_fields = []
            if not feedback1_data:
                missing_fields.append("Feedback 1")
            if not feedback2_data:
                missing_fields.append("Feedback 2")
            if not feedback3_data:
                missing_fields.append("Feedback 3")
            if not feedback4_data:
                missing_fields.append("Feedback 4")
            if not feedback5_data:
                missing_fields.append("Feedback 5")
            if not feedback6_data:
                missing_fields.append("Feedback 6")
            if not feedback7_data:
                missing_fields.append("Feedback 7")
                
            if missing_fields:
                error_message = "Please fill out the following fields: " + ", ".join(missing_fields)
                return render(request, 'tafeedback7.html', {
                    'form': form,
                    'current_page': page_number,
                    'visited_pages': request.session['visited_pages'],
                    'saved_elapsed_time': request.session.get('taproblem7_elapsed_time', 0),
                    'error_message': error_message, 
                })

            # Retrieve elapsed times for all problems
            elapsed_times = {}
            for i in range(1, 8):
                elapsed_time_key = f'taproblem{i}_elapsed_time'
                elapsed_time_value = request.POST.get(f'elapsed_time{i}')
                if elapsed_time_value:
                    try:
                        elapsed_times[elapsed_time_key] = int(elapsed_time_value)
                    except ValueError:
                        elapsed_times[elapsed_time_key] = 0
                else:
                    elapsed_times[elapsed_time_key] = request.session.get(elapsed_time_key, 0)

            # Combine all data
            complete_data = {
                **participation_data, **feedback1_data,
                **feedback2_data, **feedback3_data,
                **feedback4_data, **feedback5_data,
                **feedback6_data, **feedback7_data,
                **elapsed_times
            }

            # Save to the database
            TAFeedback.objects.create(**complete_data)

            session_keys = [
                'participation_data', 
                'taproblem1_feedback', 'taproblem2_feedback',
                'taproblem3_feedback', 
                'taproblem4_feedback', 'taproblem5_feedback',
                'taproblem6_feedback', 
            ] + [f'taproblem{i}_elapsed_time' for i in range(1, 8)]
            for key in session_keys:
                request.session.pop(key, None)

            reset_visited_pages(request)

            return redirect('success')
    else:
        initial_data = request.session.get('taproblem7_feedback', {})
        saved_elapsed_time = request.session.get('taproblem7_elapsed_time', 0)
        form = TAFeedbackForm7(initial=initial_data)

    return render(request, 'tafeedback7.html', {
        'form': form,
        'current_page': page_number,
        'visited_pages': request.session['visited_pages'],
        'saved_elapsed_time': saved_elapsed_time
    })

def index(request):
    return render(request, 'index.html')

def unauthorized_access(request):
    return render(request, 'unauthorized_access.html')

def contact(request):
    return render(request, 'contact.html')