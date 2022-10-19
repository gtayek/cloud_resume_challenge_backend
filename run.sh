# Check to make sure that .env exists
if [ ! -f .env ]
then
    echo "Please only run this command at the root directory of the project 'cloud_resume_challenge_backend'"
    exit 1
fi
source .env

source $CONDAPROFILE
conda env create -f environment.yaml
conda activate v1
# flask --app firestore_visitor_counter_api.py run --host=0.0.0.0
python firestore_visitor_counter_api.py