#!/usr/bin/env bash

VERSION=$(python -c "import modbusreader; print(modbusreader.__version__)")

echo "creating tag $VERSION"
git tag $VERSION

echo "pushing tag"
git push ${REMOTE:-origin} $VERSION

if [ -f MANIFEST ]; then
    echo "removing manifest file"
    rm MANIFEST
fi

echo "uploading package."
python setup.py sdist
twine upload dist/*