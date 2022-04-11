# DC1-POD2-SPINE2
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
- [Monitoring](#monitoring)
  - [SNMP](#snmp)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Configuration](#internal-vlan-allocation-policy-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router BGP](#router-bgp)
- [Multicast](#multicast)
- [Filters](#filters)
  - [Prefix-lists](#prefix-lists)
  - [Route-maps](#route-maps)
- [ACL](#acl)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [Quality Of Service](#quality-of-service)
- [EOS CLI](#eos-cli)

# Management

## Management Interfaces

### Management Interfaces Summary

#### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management0 | oob_management | oob | mgmt | 10.6.33.11/24 | 10.6.33.1 |

#### IPv6

| Management Interface | description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management0 | oob_management | oob | mgmt | -  | - |

### Management Interfaces Device Configuration

```eos
!
interface Management0
   description oob_management
   no shutdown
   vrf mgmt
   ip address 10.6.33.11/24
```

## Management API HTTP

### Management API HTTP Summary

| HTTP | HTTPS |
| ---- | ----- |
| False | True |

### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| mgmt | - | - |

### Management API HTTP Configuration

```eos
!
management api http-commands
   protocol https
   no shutdown
   !
   vrf mgmt
      no shutdown
```

# Authentication

## Local Users

### Local Users Summary

| User | Privilege | Role |
| ---- | --------- | ---- |
| admin | 15 | network-admin |

### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin secret sha512 $6$82gqIqw8b3nibNrk$MoZO0S8QMQN8uwnR8v48dbGrL0Ec/6q36tSx8y9IsExi4L.HtmokW9rX8VehLxhg542mNTBKqxMBF.LgnCTm4.
```

# Monitoring

## SNMP

### SNMP Configuration Summary

| Contact | Location | SNMP Traps | State |
| ------- | -------- | ---------- | ----- |
| - | AMS DC1 DC1_POD2 DC1-POD2-SPINE2 | All | Disabled |

### SNMP Device Configuration

```eos
!
snmp-server location AMS DC1 DC1_POD2 DC1-POD2-SPINE2
```

# Spanning Tree

## Spanning Tree Summary

STP mode: **none**

## Spanning Tree Device Configuration

```eos
!
spanning-tree mode none
```

# Internal VLAN Allocation Policy

## Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 1199 |

## Internal VLAN Allocation Policy Configuration

```eos
!
vlan internal order ascending range 1006 1199
```

# Interfaces

## Ethernet Interfaces

### Ethernet Interfaces Summary

#### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |

*Inherited from Port-Channel Interface

#### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1/1 | P2P_LINK_TO_DC1-POD2-LEAF1A_Ethernet30/1 | routed | - | 172.17.32.154/31 | default | 9214 | false | - | - |
| Ethernet2/1 | P2P_LINK_TO_DC1-POD2-LEAF1B_Ethernet30/1 | routed | - | 172.17.32.162/31 | default | 9214 | false | - | - |
| Ethernet3/1 | P2P_LINK_TO_DC1-POD2-LEAF2A_Ethernet30/1 | routed | - | 172.17.32.170/31 | default | 9214 | false | - | - |
| Ethernet4/1 | P2P_LINK_TO_DC1-POD2-LEAF2B_Ethernet30/1 | routed | - | 172.17.32.178/31 | default | 9214 | false | - | - |
| Ethernet5/1 | P2P_LINK_TO_DC1-POD2-LEAF3A_Ethernet30/1 | routed | - | 172.17.32.186/31 | default | 9214 | false | - | - |
| Ethernet6/1 | P2P_LINK_TO_DC1-POD2-LEAF3B_Ethernet30/1 | routed | - | 172.17.32.194/31 | default | 9214 | false | - | - |
| Ethernet7/1 | P2P_LINK_TO_DC1-POD2-LEAF4A_Ethernet30/1 | routed | - | 172.17.32.202/31 | default | 9214 | false | - | - |
| Ethernet8/1 | P2P_LINK_TO_DC1-POD2-LEAF4B_Ethernet30/1 | routed | - | 172.17.32.210/31 | default | 9214 | false | - | - |
| Ethernet9/1 | P2P_LINK_TO_DC1-POD2-LEAF5A_Ethernet30/1 | routed | - | 172.17.32.218/31 | default | 9214 | false | - | - |
| Ethernet10/1 | P2P_LINK_TO_DC1-POD2-LEAF5B_Ethernet30/1 | routed | - | 172.17.32.226/31 | default | 9214 | false | - | - |
| Ethernet11/1 | P2P_LINK_TO_DC1-POD2-LEAF6A_Ethernet30/1 | routed | - | 172.17.32.234/31 | default | 9214 | false | - | - |
| Ethernet12/1 | P2P_LINK_TO_DC1-POD2-LEAF6B_Ethernet30/1 | routed | - | 172.17.32.242/31 | default | 9214 | false | - | - |
| Ethernet13/1 | P2P_LINK_TO_DC1-POD2-LEAF7A_Ethernet30/1 | routed | - | 172.17.32.250/31 | default | 9214 | false | - | - |
| Ethernet14/1 | P2P_LINK_TO_DC1-POD2-LEAF7B_Ethernet30/1 | routed | - | 172.17.33.2/31 | default | 9214 | false | - | - |
| Ethernet15/1 | P2P_LINK_TO_DC1-POD2-LEAF8A_Ethernet30/1 | routed | - | 172.17.33.10/31 | default | 9214 | false | - | - |
| Ethernet16/1 | P2P_LINK_TO_DC1-POD2-LEAF8B_Ethernet30/1 | routed | - | 172.17.33.18/31 | default | 9214 | false | - | - |
| Ethernet17/1 | P2P_LINK_TO_DC1-POD2-LEAF9A_Ethernet30/1 | routed | - | 172.17.33.26/31 | default | 9214 | false | - | - |
| Ethernet18/1 | P2P_LINK_TO_DC1-POD2-LEAF9B_Ethernet30/1 | routed | - | 172.17.33.34/31 | default | 9214 | false | - | - |
| Ethernet19/1 | P2P_LINK_TO_DC1-POD2-LEAF10A_Ethernet30/1 | routed | - | 172.17.33.42/31 | default | 9214 | false | - | - |
| Ethernet20/1 | P2P_LINK_TO_DC1-POD2-LEAF10B_Ethernet30/1 | routed | - | 172.17.33.50/31 | default | 9214 | false | - | - |
| Ethernet21/1 | P2P_LINK_TO_DC1-POD2-LEAF11A_Ethernet30/1 | routed | - | 172.17.33.58/31 | default | 9214 | false | - | - |
| Ethernet22/1 | P2P_LINK_TO_DC1-POD2-LEAF11B_Ethernet30/1 | routed | - | 172.17.33.66/31 | default | 9214 | false | - | - |
| Ethernet23/1 | P2P_LINK_TO_DC1-POD2-LEAF12A_Ethernet30/1 | routed | - | 172.17.33.74/31 | default | 9214 | false | - | - |
| Ethernet24/1 | P2P_LINK_TO_DC1-POD2-LEAF12B_Ethernet30/1 | routed | - | 172.17.33.82/31 | default | 9214 | false | - | - |
| Ethernet25/1 | P2P_LINK_TO_DC1-POD2-LEAF13A_Ethernet30/1 | routed | - | 172.17.33.90/31 | default | 9214 | false | - | - |
| Ethernet26/1 | P2P_LINK_TO_DC1-POD2-LEAF13B_Ethernet30/1 | routed | - | 172.17.33.98/31 | default | 9214 | false | - | - |
| Ethernet27/1 | P2P_LINK_TO_DC1-POD2-LEAF14A_Ethernet30/1 | routed | - | 172.17.33.106/31 | default | 9214 | false | - | - |
| Ethernet28/1 | P2P_LINK_TO_DC1-POD2-LEAF14B_Ethernet30/1 | routed | - | 172.17.33.114/31 | default | 9214 | false | - | - |
| Ethernet29/1 | P2P_LINK_TO_SUPER-SPINE1_Ethernet6/1 | routed | - | 172.16.32.23/31 | default | 9214 | false | - | - |
| Ethernet30/1 | P2P_LINK_TO_SUPER-SPINE2_Ethernet6/1 | routed | - | 172.16.32.87/31 | default | 9214 | false | - | - |
| Ethernet31/1 | P2P_LINK_TO_SUPER-SPINE3_Ethernet6/1 | routed | - | 172.16.32.151/31 | default | 9214 | false | - | - |
| Ethernet32/1 | P2P_LINK_TO_SUPER-SPINE4_Ethernet6/1 | routed | - | 172.16.32.215/31 | default | 9214 | false | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1/1
   description P2P_LINK_TO_DC1-POD2-LEAF1A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.32.154/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet2/1
   description P2P_LINK_TO_DC1-POD2-LEAF1B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.32.162/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet3/1
   description P2P_LINK_TO_DC1-POD2-LEAF2A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.32.170/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet4/1
   description P2P_LINK_TO_DC1-POD2-LEAF2B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.32.178/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet5/1
   description P2P_LINK_TO_DC1-POD2-LEAF3A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.32.186/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet6/1
   description P2P_LINK_TO_DC1-POD2-LEAF3B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.32.194/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet7/1
   description P2P_LINK_TO_DC1-POD2-LEAF4A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.32.202/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet8/1
   description P2P_LINK_TO_DC1-POD2-LEAF4B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.32.210/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet9/1
   description P2P_LINK_TO_DC1-POD2-LEAF5A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.32.218/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet10/1
   description P2P_LINK_TO_DC1-POD2-LEAF5B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.32.226/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet11/1
   description P2P_LINK_TO_DC1-POD2-LEAF6A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.32.234/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet12/1
   description P2P_LINK_TO_DC1-POD2-LEAF6B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.32.242/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet13/1
   description P2P_LINK_TO_DC1-POD2-LEAF7A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.32.250/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet14/1
   description P2P_LINK_TO_DC1-POD2-LEAF7B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.33.2/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet15/1
   description P2P_LINK_TO_DC1-POD2-LEAF8A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.33.10/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet16/1
   description P2P_LINK_TO_DC1-POD2-LEAF8B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.33.18/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet17/1
   description P2P_LINK_TO_DC1-POD2-LEAF9A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.33.26/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet18/1
   description P2P_LINK_TO_DC1-POD2-LEAF9B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.33.34/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet19/1
   description P2P_LINK_TO_DC1-POD2-LEAF10A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.33.42/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet20/1
   description P2P_LINK_TO_DC1-POD2-LEAF10B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.33.50/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet21/1
   description P2P_LINK_TO_DC1-POD2-LEAF11A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.33.58/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet22/1
   description P2P_LINK_TO_DC1-POD2-LEAF11B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.33.66/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet23/1
   description P2P_LINK_TO_DC1-POD2-LEAF12A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.33.74/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet24/1
   description P2P_LINK_TO_DC1-POD2-LEAF12B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.33.82/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet25/1
   description P2P_LINK_TO_DC1-POD2-LEAF13A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.33.90/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet26/1
   description P2P_LINK_TO_DC1-POD2-LEAF13B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.33.98/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet27/1
   description P2P_LINK_TO_DC1-POD2-LEAF14A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.33.106/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet28/1
   description P2P_LINK_TO_DC1-POD2-LEAF14B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.33.114/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet29/1
   description P2P_LINK_TO_SUPER-SPINE1_Ethernet6/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.32.23/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet30/1
   description P2P_LINK_TO_SUPER-SPINE2_Ethernet6/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.32.87/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet31/1
   description P2P_LINK_TO_SUPER-SPINE3_Ethernet6/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.32.151/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet32/1
   description P2P_LINK_TO_SUPER-SPINE4_Ethernet6/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.32.215/31
   ptp enable
   service-profile P2P-QOS-PROFILE
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 10.4.32.12/32 |

#### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |


### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   no shutdown
   ip address 10.4.32.12/32
```

# Routing
## Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

## IP Routing

### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | true |
| mgmt | false |

### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf mgmt
```
## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false |
| mgmt | false |

## Static Routes

### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP             | Exit interface      | Administrative Distance       | Tag               | Route Name                    | Metric         |
| --- | ------------------ | ----------------------- | ------------------- | ----------------------------- | ----------------- | ----------------------------- | -------------- |
| mgmt  | 0.0.0.0/0 |  10.6.33.1  |  -  |  1  |  -  |  -  |  - |

### Static Routes Device Configuration

```eos
!
ip route vrf mgmt 0.0.0.0/0 10.6.33.1
```

## Router BGP

### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 64702|  10.4.32.12 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| graceful-restart restart-time 300 |
| graceful-restart |
| maximum-paths 4 ecmp 4 |

### Router BGP Peer Groups

#### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- |
| 172.16.32.22 | 64501 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.16.32.86 | 64502 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.16.32.150 | 64503 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.16.32.214 | 64504 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.32.155 | 65001 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.32.163 | 65001 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.32.171 | 65002 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.32.179 | 65002 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.32.187 | 65003 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.32.195 | 65003 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.32.203 | 65004 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.32.211 | 65004 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.32.219 | 65005 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.32.227 | 65005 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.32.235 | 65006 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.32.243 | 65006 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.32.251 | 65007 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.33.3 | 65007 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.33.11 | 65008 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.33.19 | 65008 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.33.27 | 65009 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.33.35 | 65009 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.33.43 | 65010 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.33.51 | 65010 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.33.59 | 65011 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.33.67 | 65011 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.33.75 | 65012 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.33.83 | 65012 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.33.91 | 65013 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.33.99 | 65013 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.33.107 | 65014 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.33.115 | 65014 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |

### Router BGP Device Configuration

```eos
!
router bgp 64702
   router-id 10.4.32.12
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 4 ecmp 4
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS password 7 AQQvKeimxJu+uGQ/yYvv9w==
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor 172.16.32.22 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.32.22 remote-as 64501
   neighbor 172.16.32.22 description SUPER-SPINE1_Ethernet6/1
   neighbor 172.16.32.86 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.32.86 remote-as 64502
   neighbor 172.16.32.86 description SUPER-SPINE2_Ethernet6/1
   neighbor 172.16.32.150 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.32.150 remote-as 64503
   neighbor 172.16.32.150 description SUPER-SPINE3_Ethernet6/1
   neighbor 172.16.32.214 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.32.214 remote-as 64504
   neighbor 172.16.32.214 description SUPER-SPINE4_Ethernet6/1
   neighbor 172.17.32.155 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.32.155 remote-as 65001
   neighbor 172.17.32.155 description DC1-POD2-LEAF1A_Ethernet30/1
   neighbor 172.17.32.163 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.32.163 remote-as 65001
   neighbor 172.17.32.163 description DC1-POD2-LEAF1B_Ethernet30/1
   neighbor 172.17.32.171 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.32.171 remote-as 65002
   neighbor 172.17.32.171 description DC1-POD2-LEAF2A_Ethernet30/1
   neighbor 172.17.32.179 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.32.179 remote-as 65002
   neighbor 172.17.32.179 description DC1-POD2-LEAF2B_Ethernet30/1
   neighbor 172.17.32.187 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.32.187 remote-as 65003
   neighbor 172.17.32.187 description DC1-POD2-LEAF3A_Ethernet30/1
   neighbor 172.17.32.195 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.32.195 remote-as 65003
   neighbor 172.17.32.195 description DC1-POD2-LEAF3B_Ethernet30/1
   neighbor 172.17.32.203 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.32.203 remote-as 65004
   neighbor 172.17.32.203 description DC1-POD2-LEAF4A_Ethernet30/1
   neighbor 172.17.32.211 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.32.211 remote-as 65004
   neighbor 172.17.32.211 description DC1-POD2-LEAF4B_Ethernet30/1
   neighbor 172.17.32.219 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.32.219 remote-as 65005
   neighbor 172.17.32.219 description DC1-POD2-LEAF5A_Ethernet30/1
   neighbor 172.17.32.227 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.32.227 remote-as 65005
   neighbor 172.17.32.227 description DC1-POD2-LEAF5B_Ethernet30/1
   neighbor 172.17.32.235 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.32.235 remote-as 65006
   neighbor 172.17.32.235 description DC1-POD2-LEAF6A_Ethernet30/1
   neighbor 172.17.32.243 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.32.243 remote-as 65006
   neighbor 172.17.32.243 description DC1-POD2-LEAF6B_Ethernet30/1
   neighbor 172.17.32.251 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.32.251 remote-as 65007
   neighbor 172.17.32.251 description DC1-POD2-LEAF7A_Ethernet30/1
   neighbor 172.17.33.3 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.33.3 remote-as 65007
   neighbor 172.17.33.3 description DC1-POD2-LEAF7B_Ethernet30/1
   neighbor 172.17.33.11 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.33.11 remote-as 65008
   neighbor 172.17.33.11 description DC1-POD2-LEAF8A_Ethernet30/1
   neighbor 172.17.33.19 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.33.19 remote-as 65008
   neighbor 172.17.33.19 description DC1-POD2-LEAF8B_Ethernet30/1
   neighbor 172.17.33.27 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.33.27 remote-as 65009
   neighbor 172.17.33.27 description DC1-POD2-LEAF9A_Ethernet30/1
   neighbor 172.17.33.35 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.33.35 remote-as 65009
   neighbor 172.17.33.35 description DC1-POD2-LEAF9B_Ethernet30/1
   neighbor 172.17.33.43 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.33.43 remote-as 65010
   neighbor 172.17.33.43 description DC1-POD2-LEAF10A_Ethernet30/1
   neighbor 172.17.33.51 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.33.51 remote-as 65010
   neighbor 172.17.33.51 description DC1-POD2-LEAF10B_Ethernet30/1
   neighbor 172.17.33.59 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.33.59 remote-as 65011
   neighbor 172.17.33.59 description DC1-POD2-LEAF11A_Ethernet30/1
   neighbor 172.17.33.67 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.33.67 remote-as 65011
   neighbor 172.17.33.67 description DC1-POD2-LEAF11B_Ethernet30/1
   neighbor 172.17.33.75 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.33.75 remote-as 65012
   neighbor 172.17.33.75 description DC1-POD2-LEAF12A_Ethernet30/1
   neighbor 172.17.33.83 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.33.83 remote-as 65012
   neighbor 172.17.33.83 description DC1-POD2-LEAF12B_Ethernet30/1
   neighbor 172.17.33.91 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.33.91 remote-as 65013
   neighbor 172.17.33.91 description DC1-POD2-LEAF13A_Ethernet30/1
   neighbor 172.17.33.99 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.33.99 remote-as 65013
   neighbor 172.17.33.99 description DC1-POD2-LEAF13B_Ethernet30/1
   neighbor 172.17.33.107 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.33.107 remote-as 65014
   neighbor 172.17.33.107 description DC1-POD2-LEAF14A_Ethernet30/1
   neighbor 172.17.33.115 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.33.115 remote-as 65014
   neighbor 172.17.33.115 description DC1-POD2-LEAF14B_Ethernet30/1
   redistribute connected route-map RM-CONN-2-BGP
   !
   address-family ipv4
      neighbor IPv4-UNDERLAY-PEERS activate
```

# Multicast

# Filters

## Prefix-lists

### Prefix-lists Summary

#### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 10.4.32.0/24 eq 32 |

### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 10.4.32.0/24 eq 32
```

## Route-maps

### Route-maps Summary

#### RM-CONN-2-BGP

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | permit | match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY |

### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
```

# ACL

# VRF Instances

## VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| mgmt | disabled |

## VRF Instances Device Configuration

```eos
!
vrf instance mgmt
```

# Quality Of Service

# EOS CLI

```eos
!
interface Loopback1111
  description Loopback created from raw_eos_cli under platform_settings vEOS-LAB in AMS.yml

```
