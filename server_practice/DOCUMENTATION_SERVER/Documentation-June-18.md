#### June 18, 2021

### Learned:

1. __Formatting__

    Formatting basically means to alter data in a page. Very useful in making **dynamic** webpages.

    `<p>{fname:} is {eligible:} to vote.</p>` This is the line to be formatted; `{fname:}` and `{eligible:}` can be called variables as their values can be changed as data is posted to them. 

    `new_file = open("verify.html").read().format(fname= first_name, eligible = eligibility)`

    Here, the first thing that happens is that the file _verify.html_ is opened then the texts inside it is read by _read()_ function and _.format()_ feeds the corresponding `{fname:}` and `{eligible:}` data to them. 
    
    The other __important__ thing to notice here is that the _verify.html_ html file is converted to a string.

2. Creating a new HTML file

    Once this 
    ```python
    new_file = open("verify.html").read().format(fname= first_name, eligible = eligibility)
    ``` 
    is called, the changes happen in the _verify.html_ file. If we post this as our _self.path_ file, then it **will successfully run only once.**. 

    So, in order to avoid this, a clone of _verify.html_ file is made as _verify2.html_ by this code:
    ```python
    index = open("verify2.html", "w").write(new_file)
    ``` 
    
    _The index variable is unwanted here._ 
3. Returning the clone html file is as easy as feeding the file to _self.path_. 


### Bootstrap

Bootstrap is a framework that assists in building a better webpage with ease and multiple built-in cool functions. 

#### Learned
1. Go to [getting started](https://getbootstrap.com/docs/3.4/getting-started/) and copy whatever in the Bootstrap CDN section. 
2. The following things must be inside the `<head>` element.
```html
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap-theme.min.css" integrity="sha384-6pzBo3FDv/PJ8r2KRkGHifhEocL+1X2rVCTTkUfGk7/0pbek5mMa1upzvWbrUbOZ" crossorigin="anonymous">
```
The follwing line of code must be before `</body>` element.
```html
<script src="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js" integrity="sha384-aJ21OjlMXNL5UyIl/XNwTMqvzeRMZH2w8c5cRVpzpU8Y5bApTppSuUkhZXN0VxHd" crossorigin="anonymous"></script>
```
3. Now there are tons of things to add in a webpage from the [components](https://getbootstrap.com/docs/3.4/components/) page. 



### Key take aways:

1. Since `open()` returns a file object, it is not always necessary to assign a variable to it. It can even run unassigned. 
2. 


