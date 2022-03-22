from flask import Flask, render_template, redirect, request, Blueprint
from modules.animal import Animal
from modules.owner import Owner
from modules.vet import Vet

from repositories.owner_repo import select_last_name
from repositories.animal_repo import select_animal_by_owner

from repositories import animal_repo
from repositories import owner_repo
from repositories import vet_repo

vet_blueprint = Blueprint("animal", __name__)

# route to get to the front page /new_client to add a new animal
@vet_blueprint.route("/new_client", methods =['GET'])
def new_client():

    vets = vet_repo.select_all()
    return render_template("/new.html", vets = vets)

# route to save the client after inputting details to form
@vet_blueprint.route("/new_client/save_new_client", methods=['POST'])
def save_new_client():

    name = request.form["name"]
    dob = request.form["DOB"]
    species = request.form["species"]
    treatments = request.form["treatments"]
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    number = request.form ["number"]
    vet_id = request.form["vet_id"]

    vet = vet_repo.select_by_id(vet_id)    

    owner = Owner(first_name, last_name, number)
    animal = Animal(name, dob, species, treatments, owner, vet, id)
    animal.vet_id = vet_id
    saved_owner = owner_repo.save(owner)
    animal.owner_id = saved_owner.id
    animal_repo.save(animal)


    return redirect('/submit')

# route which functions when we click on submit when we save an animal
@vet_blueprint.route("/submit", methods =['GET'])
def submit():
    return render_template("/submit.html")

# route which functions when we click on search in the nav
@vet_blueprint.route("/search", methods =['GET'])
def search_here():

    return render_template("/search.html")

# route which functions when we click on the owner, which is being listed after the last funciton
@vet_blueprint.route("/search/<owner_id>", methods =['GET'])
def display_client(owner_id):

    owner = owner_repo.select_by_id(owner_id)
    animals = animal_repo.select_animal_by_owner(owner)

    return render_template("/view_client.html",owner = owner, animals = animals)


@vet_blueprint.route("/search/search_action", methods =['POST'])
def search_for_client():

    last_name = request.form["last_name"]
    owners = owner_repo.select_last_name(last_name)

    # animal = animal_repo.select_animal(owner_id)

    return render_template('/view_clients.html',owners=owners)


# function which runs when we click on add button
@vet_blueprint.route("/search_action/add_animal", methods=['GET'])
def add_animal():

    return render_template ("/add_animal.html")




# function which runs when we click on update button, function actually leads to the update.html page ! 
# DO NOT CHANGE CODE !
@vet_blueprint.route("/search_action/update/<owner_id>", methods=['GET'])
def update_client(owner_id):

    # TO update the data in the database, you need to get the data, via ID or lastname,.. 
    # then After instantiating the class of the object from the database.
    # animal = animal_repo.select_by_id(ID)
    # then UPDATE the items in the class such as animan.name = request.form["name"]
    # after updating all of the variables stored in the class run the animal_repo.update(animal) making sure to pass in the full new class object
     
    return render_template ("/update.html",owner_id = owner_id)


# function which runs when we submit the updated client
# Submit button works, however client won't update yet
@vet_blueprint.route("/update_action/<owner_id>", methods=['POST'])
def edit_client(owner_id):


    owner = owner_repo.select_by_id(owner_id)

    # name = request.form["name"]
    # dob = request.form["DOB"]
    # species = request.form["species"]
    # treatments = request.form["treatments"]
    owner.first_name = request.form["first_name"]
    # owner.first_name = request.form["first_name"]
    owner.last_name = request.form["last_name"]
    owner.number = request.form ["number"]
    # # vet_id = request.form["vet_id"] not listed in actual update form

    # animal = Animal(name, dob, species, treatments)


    owner_repo.update(owner)
    # # animal.vet_id = vet_id.
    # saved_owner = owner_repo.save(owner)
    # animal.owner_id = saved_owner.id
    # animal_repo.save(animal)

    return redirect ('/submit')


# function which runs when we click on delete and redirect to Home
# when clicking button it does redirect to Home, but does not yet delete animal
@vet_blueprint.route("/search_action/delete", methods=['GET'])
def delete_all():

    # animal_repo.delete()
    # owner_repo.delete()

    return render_template ("/index.html")




