from conans import ConanFile, tools
from conans import __version__ as conan_version
from conans.model.version import Version
import os


class StrawberryperlConan(ConanFile):
    name = "strawberryperl"
    version = "5.26.2.1"
    license = "GNU Public License or the Artistic License"
    url = "https://github.com/kwallner/conan-strawberryperl"
    settings = {"os_build": ["Windows"], "arch_build" : ["x86_64", "x86"]}
    description = "Strawbery Perl for Windows. Useful as build_require"
    no_copy_source = True

    def source(self):
        tools.download("http://strawberryperl.com/download/%s/strawberry-perl-%s-64bit-portable.zip" % (self.version, self.version), "%s.zip" % "x86_64")
        tools.download("http://strawberryperl.com/download/%s/strawberry-perl-%s-32bit-portable.zip" % (self.version, self.version), "%s.zip" % "x86")

    def build(self):
        tools.unzip(os.path.join(self.source_folder,  "%s.zip" % self.settings.arch_build))
 
    def package(self):
        self.copy("*", keep_path=True, excludes = "*.zip")
        self.copy("licenses/License.rtf*", dst=".", keep_path=False, ignore_case=True)

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, "perl", "bin"))
        self.env_info.PATH.append(os.path.join(self.package_folder, "c", "bin"))
