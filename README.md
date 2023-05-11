# django-geonode-userdetails
## django-geonode-userdetails
This app exposes a small API endpoint that provide details regarding the current authenticated user.
It is based on Django REST Framework.
It is released under GNU-GPL licence version 3.

## Add Django app. to Geonode setup
### Manual install
Here below are listed the instruction for install:

1. If you are using `docker`, stop services

    ```console
    docker-compose down
    ```

2. Add "gdc" to your INSTALLED_APPS by adding the following lines at the end of `./geonode/settings.py` file:

    ```python
    # Addition of gdc app
    INSTALLED_APPS += ('geonode.userdetails',)
    ```

3. Include the gdc URLconf in `./geonode/urls.py` file like this:

    ```python
    if "geonode.userdetails" in settings.INSTALLED_APPS:
        urlpatterns += [  # '',
            url(r'^gdc/', include('geonode.userdetails.urls')),
        ]
    ```

4. Move `userdetails` folder inside `./geonode` django project folder:


5. If you are using `docker`, rebuild geonode and restart services (this may stop the web site for a while):

    ```console
    docker-compose down && docker-compose build && docker-compose up -d
    ```

6. Once geonode has restarted, authenticated users can reach the endpoints under `/userdetails` to fetch information regarding their profile using **GET** queries. Result is returned in JSON format.

### Example setup

You can find an example of a geonode setup with GDC app in this repo: [django-geonode-dev](https://github.com/phardy-egis/django-geonode-dev.git). 