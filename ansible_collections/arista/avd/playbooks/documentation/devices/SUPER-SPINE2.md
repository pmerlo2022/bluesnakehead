# SUPER-SPINE2
# Table of Contents
<!-- toc -->

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

<!-- toc -->
# Management

## Management Interfaces

### Management Interfaces Summary

#### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management0 | oob_management | oob | mgmt | 10.6.0.2/24 | 10.6.0.1 |

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
   ip address 10.6.0.2/24
```

## Management API HTTP

### Management API HTTP Summary

| HTTP | HTTPS |
| ---------- | ---------- |
| default | true |

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
| - | AMS SUPER-SPINE2 | All | Disabled |

### SNMP Device Configuration

```eos
!
snmp-server location AMS SUPER-SPINE2
```

# Spanning Tree

## Spanning Tree Summary

STP mode: **none**

### Global Spanning-Tree Settings


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
| Ethernet1/1 | P2P_LINK_TO_DC1-POD1-SPINE1_Ethernet30/1 | routed | - | 172.16.1.8/31 | default | 9214 | false | - | - |
| Ethernet2/1 | P2P_LINK_TO_DC1-POD1-SPINE2_Ethernet30/1 | routed | - | 172.16.1.10/31 | default | 9214 | false | - | - |
| Ethernet3/1 | P2P_LINK_TO_DC1-POD1-SPINE3_Ethernet30/1 | routed | - | 172.16.1.12/31 | default | 9214 | false | - | - |
| Ethernet4/1 | P2P_LINK_TO_DC1-POD1-SPINE4_Ethernet30/1 | routed | - | 172.16.1.14/31 | default | 9214 | false | - | - |
| Ethernet5/1 | P2P_LINK_TO_DC1-POD2-SPINE1_Ethernet30/1 | routed | - | 172.16.2.64/31 | default | 9214 | false | - | - |
| Ethernet6/1 | P2P_LINK_TO_DC1-POD2-SPINE2_Ethernet30/1 | routed | - | 172.16.2.66/31 | default | 9214 | false | - | - |
| Ethernet7/1 | P2P_LINK_TO_DC1-POD2-SPINE3_Ethernet30/1 | routed | - | 172.16.2.68/31 | default | 9214 | false | - | - |
| Ethernet8/1 | P2P_LINK_TO_DC1-POD2-SPINE4_Ethernet30/1 | routed | - | 172.16.2.70/31 | default | 9214 | false | - | - |
| Ethernet9/1 | P2P_LINK_TO_DC2-POD1-SPINE1_Ethernet30/1 | routed | - | 172.16.32.64/31 | default | 9214 | false | - | - |
| Ethernet10/1 | P2P_LINK_TO_DC2-POD1-SPINE2_Ethernet30/1 | routed | - | 172.16.32.66/31 | default | 9214 | false | - | - |
| Ethernet11/1 | P2P_LINK_TO_DC2-POD1-SPINE3_Ethernet30/1 | routed | - | 172.16.32.68/31 | default | 9214 | false | - | - |
| Ethernet12/1 | P2P_LINK_TO_DC2-POD1-SPINE4_Ethernet30/1 | routed | - | 172.16.32.70/31 | default | 9214 | false | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1/1
   description P2P_LINK_TO_DC1-POD1-SPINE1_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.1.8/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet2/1
   description P2P_LINK_TO_DC1-POD1-SPINE2_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.1.10/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet3/1
   description P2P_LINK_TO_DC1-POD1-SPINE3_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.1.12/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet4/1
   description P2P_LINK_TO_DC1-POD1-SPINE4_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.1.14/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet5/1
   description P2P_LINK_TO_DC1-POD2-SPINE1_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.2.64/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet6/1
   description P2P_LINK_TO_DC1-POD2-SPINE2_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.2.66/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet7/1
   description P2P_LINK_TO_DC1-POD2-SPINE3_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.2.68/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet8/1
   description P2P_LINK_TO_DC1-POD2-SPINE4_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.2.70/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet9/1
   description P2P_LINK_TO_DC2-POD1-SPINE1_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.32.64/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet10/1
   description P2P_LINK_TO_DC2-POD1-SPINE2_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.32.66/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet11/1
   description P2P_LINK_TO_DC2-POD1-SPINE3_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.32.68/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet12/1
   description P2P_LINK_TO_DC2-POD1-SPINE4_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.32.70/31
   ptp enable
   service-profile P2P-QOS-PROFILE
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 10.4.27.2/32 |

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
   ip address 10.4.27.2/32
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
| default | true|| mgmt | false |

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
| default | false || mgmt | false |


## Static Routes

### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP             | Exit interface      | Administrative Distance       | Tag               | Route Name                    | Metric         |
| --- | ------------------ | ----------------------- | ------------------- | ----------------------------- | ----------------- | ----------------------------- | -------------- |
| mgmt  | 0.0.0.0/0 |  10.6.0.1  |  -  |  1  |  -  |  -  |  - |

### Static Routes Device Configuration

```eos
!
ip route vrf mgmt 0.0.0.0/0 10.6.0.1
```

## Router BGP

### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 64102|  10.4.27.2 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| graceful-restart restart-time 300 |
| graceful-restart |
| maximum-paths 16 ecmp 16 |

### Router BGP Peer Groups

#### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

### BGP Neighbors

| Neighbor | Remote AS | VRF | Send-community | Maximum-routes |
| -------- | --------- | --- | -------------- | -------------- |
| 172.16.1.9 | 65001.100 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.16.1.11 | 65001.102 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.16.1.13 | 65001.100 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.16.1.15 | 65001.100 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.16.2.65 | 65001.200 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.16.2.67 | 65001.200 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.16.2.69 | 65001.200 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.16.2.71 | 65001.200 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.16.32.65 | 65002.100 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.16.32.67 | 65002.100 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.16.32.69 | 65002.100 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |
| 172.16.32.71 | 65002.100 | default | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS |

### Router BGP EVPN Address Family

#### Router BGP EVPN MAC-VRFs

#### Router BGP EVPN VRFs

### Router BGP Device Configuration

```eos
!
router bgp 64102
   router-id 10.4.27.2
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 16 ecmp 16
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor 172.16.1.9 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.1.9 remote-as 65001.100
   neighbor 172.16.1.9 description DC1-POD1-SPINE1_Ethernet30/1
   neighbor 172.16.1.11 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.1.11 remote-as 65001.102
   neighbor 172.16.1.11 description DC1-POD1-SPINE2_Ethernet30/1
   neighbor 172.16.1.13 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.1.13 remote-as 65001.100
   neighbor 172.16.1.13 description DC1-POD1-SPINE3_Ethernet30/1
   neighbor 172.16.1.15 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.1.15 remote-as 65001.100
   neighbor 172.16.1.15 description DC1-POD1-SPINE4_Ethernet30/1
   neighbor 172.16.2.65 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.2.65 remote-as 65001.200
   neighbor 172.16.2.65 description DC1-POD2-SPINE1_Ethernet30/1
   neighbor 172.16.2.67 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.2.67 remote-as 65001.200
   neighbor 172.16.2.67 description DC1-POD2-SPINE2_Ethernet30/1
   neighbor 172.16.2.69 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.2.69 remote-as 65001.200
   neighbor 172.16.2.69 description DC1-POD2-SPINE3_Ethernet30/1
   neighbor 172.16.2.71 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.2.71 remote-as 65001.200
   neighbor 172.16.2.71 description DC1-POD2-SPINE4_Ethernet30/1
   neighbor 172.16.32.65 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.32.65 remote-as 65002.100
   neighbor 172.16.32.65 description DC2-POD1-SPINE1_Ethernet30/1
   neighbor 172.16.32.67 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.32.67 remote-as 65002.100
   neighbor 172.16.32.67 description DC2-POD1-SPINE2_Ethernet30/1
   neighbor 172.16.32.69 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.32.69 remote-as 65002.100
   neighbor 172.16.32.69 description DC2-POD1-SPINE3_Ethernet30/1
   neighbor 172.16.32.71 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.32.71 remote-as 65002.100
   neighbor 172.16.32.71 description DC2-POD1-SPINE4_Ethernet30/1
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
| 10 | permit 10.4.27.0/24 eq 32 |

### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 10.4.27.0/24 eq 32
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
