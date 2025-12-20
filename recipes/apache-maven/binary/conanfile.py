from conan import ConanFile
from conan.tools.files import get, copy

required_conan_version = ">=2.10.0"

class ApacheMavenConan(ConanFile):
    name = "apache-maven"
    version = "3.9.12"
    license = ("Apache License 2.0")
    homepage = "https://maven.apache.org/download.cgi"
    description = "Apache Maven is a software project management and comprehension tool."
    topics = ("maven", "build", "java")
    settings = "os", "arch"

    def build(self):
        get(self, **self.conan_data["sources"][self.version][str(self.settings.os)][str(self.settings.arch)],
            destination=self.source_folder, strip_root=True)
        
    def package(self):
        copy(self, "*", src=self.source_folder, dst=self.package_folder)