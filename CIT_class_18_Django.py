# Creative IT Class #18 Topic: Profile Update Operation Date: 19/06/2023
# In The HTML Form
'''
<form method="POST" enctype="multipart/form-data">
                    {% csrf_token %}
                    <div class="form-group">
                        <label>name</label>
                        <input type="text" name="name" value="{{ prof.name }}" class="form-control" placeholder="Enter Name">
                        <br>
                        <label>Email address</label>
                        <input type="email" name="email" value="{{ prof.email }}" class="form-control" placeholder="Enter email">
                        <br>
                        <label>Phone</label>
                        <input type="text" name="phone" value="{{ prof.phone }}" class="form-control" placeholder="Enter Phone">
                        <br>
                        <label>Age</label>
                        <input type="text" name="age" value="{{ prof.age }}" class="form-control" placeholder="Enter Age">
                        <br>
                        <label>Address</label>
                        <input type="text" name="address" value="{{ prof.address }}" class="form-control" placeholder="Enter Address">
                        <br>
                        <label>Date of Birth</label>
                        <input type="datetime-local" name="dob" value="{{ prof.dob }}" class="form-control" placeholder="Enter Date of Birth">
                        <br>
                        <label>Image</label>
                        <input type="file" name="image" class="form-control" placeholder="Upload Image">
                        <img src="{{ prof.image.url }}" height="50px" alt="">
                        <br>
                        <label>Religion</label>
                        <select name="religion" class="custom-select">
                        <option value="{{ prof.religion }}">{{ prof.religion }}</option>
                        <option value="Islam">Islam</option>
                        <option value="Hinduism">Hinduism</option>
                        <option value="Buddhism">Buddhism</option>
                        <option value="Judaism">Judaism</option>
                        <option value="Christianity">Christianity</option>
                        </select>
                        <br><br>
                        <label>Gender</label>
                        <select name="gender" class="custom-select">
                        <option value="{{ prof.gender }}">{{ prof.gender }}</option>
                        <option value="Male">Male</option>
                        <option value="Female">Female</option>
                        <option value="Others">Others</option>
                        </select>
                    </div>
                    <br>
                    <button type="submit" class="btn btn-primary">Update</button>
                </form>
'''

# In The App/urls.py
'''
path('update/<id>/', update, name='update')
'''

# In the views.py
'''

# Import "os" top of views.py for Image/File remove operation

def update(Request, id):
    prof = Profile.objects.get(id=id)
    if Request.method == 'POST':
        # if len(Request.FILES.get('image')) !=0:
        if Request.FILES.get('image') != None:
            if prof.image != 'default/no_img.jpg':
                os.remove(prof.image.path)
            prof.name       = Request.POST.get('name')
            prof.image      = Request.FILES.get('image')
            prof.email      = Request.POST.get('email')
            prof.age        = Request.POST.get('age')
            prof.address    = Request.POST.get('address')
            prof.phone      = Request.POST.get('phone')
            prof.dob        = Request.POST.get('dob')
            prof.religion   = Request.POST.get('religion')
            prof.gender     = Request.POST.get('gender')
            prof.save()
            messages.success(Request, 'Profile Updated Successfully')
            return redirect('main')
        else:
            prof.name       = Request.POST.get('name')
            prof.email      = Request.POST.get('email')
            prof.age        = Request.POST.get('age')
            prof.address    = Request.POST.get('address')
            prof.phone      = Request.POST.get('phone')
            prof.dob        = Request.POST.get('dob')
            prof.religion   = Request.POST.get('religion')
            prof.gender     = Request.POST.get('gender')
            prof.save()
            messages.success(Request, 'Profile Updated Successfully')
            return redirect('main')
    return render(Request, 'update.html', locals())
'''
