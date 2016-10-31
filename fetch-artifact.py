import argparse, requests

parser = argparse.ArgumentParser(description='The CircleCI artifact deployment tool.')
parser.add_argument('-b', '--branch', help='Which branch to deploy (defaults to master)', default='master')
parser.add_argument('-u', '--user', help='The CircleCI username to look under')
parser.add_argument('-p', '--project', help='Which project to deploy')
parser.add_argument('-t', '--token', help='The CircleCI API token to use')
parser.add_argument('-v', '--vcs', help='The VCS type (defaults to github)', default='github')

args = parser.parse_args()

branch = args.branch
user = args.user
project = args.project
token = args.token
vcs = args.vcs

circleci = 'https://circleci.com/api/v1.1/project/' + vcs + '/' + user + '/' + project + '/latest/artifacts?circle-token=' + token + '&branch=' + branch

print 'Checking for latest build...'

response = requests.get( circleci )
json = response.json()
data = json[0]

url = data['url']

print 'Fetching artifact from ' + url + ' ...'

url += '?circle-token=' + token

response = requests.get( url, stream=True )

filename = 'latest.tar.gz'
chunk_size = 1024

with open( filename, 'wb' ) as fd:
  for chunk in response.iter_content( chunk_size ):
    fd.write( chunk )

print 'Artifact retrieved and saved as ' + filename + '.'
