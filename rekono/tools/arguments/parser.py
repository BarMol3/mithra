from findings.models import (OSINT, Enumeration, Exploit, Host, HttpEndpoint,
                             Technology, Vulnerability)
from tasks.enums import ParameterKey
from tasks.models import Parameter
from tools.arguments import checker
from tools.arguments.constants import PORT, PORTS, PORTS_COMMAS, TARGET, URL
from tools.arguments.url import Url


def osint(osint: OSINT) -> dict:
    if osint.data_type in [OSINT.DataType.IP, OSINT.DataType.DOMAIN]:
        return {
            TARGET: osint.data,
        }
    return {}


def host(host: Host) -> dict:
    return {
        TARGET: host.address
    }


def enumeration(enumeration: Enumeration, accumulated: dict = {}) -> dict:
    output = {
        TARGET: enumeration.host.address,
        PORT: enumeration.port,
        PORTS: [enumeration.port]
    }
    if accumulated and PORTS in accumulated:
        output[PORTS] = accumulated[PORTS]
        output[PORTS].append(enumeration.port)
    output[PORTS_COMMAS] = ','.join([str(port) for port in output[PORTS]])
    return output


def http_endpoint(http_endpoint: HttpEndpoint):
    output = enumeration(http_endpoint.enumeration)
    output[ParameterKey.HTTP_ENDPOINT.name.lower()] = http_endpoint.endpoint
    return output


def technology(technology: Technology) -> dict:
    output = enumeration(technology.enumeration)
    output[ParameterKey.TECHNOLOGY.name.lower()] = technology.name
    if technology.version:
        output[ParameterKey.VERSION.name.lower()] = technology.version
    return output


def vulnerability(vulnerability: Vulnerability) -> dict:
    output = {}
    if vulnerability.enumeration:
        output = enumeration(vulnerability.enumeration)
    elif vulnerability.technology:
        output = technology(vulnerability.technology)
    if vulnerability.cve:
        output[ParameterKey.CVE.name.lower()] = vulnerability.cve
    return output


def exploit(exploit: Exploit) -> dict:
    output = vulnerability(exploit.vulnerability)
    output[ParameterKey.EXPLOIT.name.lower()] = exploit.name
    return output


def url(url: Url) -> dict:
    return {
        URL: url.value
    }


def parameter(parameter: Parameter) -> dict:
    checker.check_parameter(parameter)
    return {
        ParameterKey(parameter.key).name.lower(): parameter.value
    }


def parameter_multiple(parameter: Parameter, accumulated: dict = {}) -> dict:
    checker.check_parameter(parameter)
    output = {
        ParameterKey(parameter.key).name.lower() + '_data': [parameter.value],
        ParameterKey(parameter.key).name.lower(): parameter.value
    }
    if accumulated:
        aux = accumulated[ParameterKey(parameter.key).name.lower() + '_data']
        aux.append(parameter.value)
        output = {
            ParameterKey(parameter.key).name.lower(): ','.join(aux)
        }
    return output
