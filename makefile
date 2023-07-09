# See: https://www.gnu.org/software/make/manual/make.html

DOC_TARGET_DIR=_build
TESTFILE_SOURCE_DIR=tests_pytest
DOC_DIR=docs

$(DOC_TARGET_DIR)/$(TESTFILE_SOURCE_DIR)/*.html : $(TESTFILE_SOURCE_DIR)/*.*
	pycco -i -d $(DOC_TARGET_DIR) -p -u --escape-html $(TESTFILE_SOURCE_DIR)/*.*

# Run the documentation generation on the .c files - eyeball them afterwards
$(DOC_TARGET_DIR)/*mod*_c.html: $(TESTFILE_SOURCE_DIR)/*mod*.c
	pycco -i -d $(DOC_TARGET_DIR) -p -u  $(TESTFILE_SOURCE_DIR)/*mod*.c

$(DOC_DIR)/main_py.html: pycco/main.py pycco/jsp.jpg
	pycco -d $(DOC_DIR) -u  pycco/main.py
	cp pycco/jsp.jpg $(DOC_DIR)

clean_testfiles:
	rm -fr $(DOC_TARGET_DIR)/$(TESTFILE_SOURCE_DIR)/*.*
	rmdir $(DOC_TARGET_DIR)/$(TESTFILE_SOURCE_DIR)/
	rm -rf $(DOC_TARGET_DIR)/*.*
	rmdir $(DOC_TARGET_DIR)
