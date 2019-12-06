@Library('ecdc-pipeline')
import ecdcpipeline.ContainerBuildNode
import ecdcpipeline.ConanPackageBuilder

conan_pkg_channel = "stable"

container_build_nodes = [
  'centos': ContainerBuildNode.getDefaultContainerBuildNode('centos7')
]

package_builder = new ConanPackageBuilder(this, container_build_nodes, conan_pkg_channel)
package_builder.defineRemoteUploadNode('centos')

builders = package_builder.createPackageBuilders { container ->
  package_builder.addConfiguration(container, [
    'settings': [
      'spdlog-graylog:build_type': 'Release'
    ]
  ])
}

node {
  checkout scm

  try {
    parallel builders
  } catch (e) {
    pipeline_builder.handleFailureMessages()
    throw e
  }

  // Delete workspace when build is done.
  cleanWs()
}
